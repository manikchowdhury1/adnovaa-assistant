# Live site-data fetcher for the Adnovaa Assistant.
# ALL answers come from adnovaa.com itself (WP REST + Woo Store API), cached
# for 10 minutes — so when the website is updated, the bot's answers update
# automatically. Nothing about the site's content is hardcoded here.

import html
import json
import re
import time

import requests

SITE = "https://adnovaa.com"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
TTL = 600  # seconds


def _get(path, params=None):
    r = requests.get(SITE + path, params=params or {}, headers=UA, timeout=12)
    r.raise_for_status()
    return json.loads(r.content.decode("utf-8-sig"))  # site emits a BOM


def clean_text(raw_html):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw_html or "", flags=re.S | re.I)
    t = re.sub(r"</(p|h1|h2|h3|h4|li|div|tr)>", "\n", t, flags=re.I)
    t = re.sub(r"<li[^>]*>", "\n• ", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


def chunk_text(text, title, url):
    """Split page text into retrievable chunks of ~120-900 chars.

    Numbered-question boundaries (FAQ pages: "7. How do I pay...") are
    hard split points first, so each Q&A is its own retrievable unit and
    a commission answer never arrives glued to a refund answer.
    """
    chunks = []
    for segment in re.split(r"\n\s*(?=\d{1,2}\.\s)", text):
        chunks.extend(_pack(segment, title, url))
    return chunks


def _pack(text, title, url):
    chunks, buf = [], ""
    for para in re.split(r"\n\s*\n|\n", text):
        para = para.strip()
        if not para:
            continue
        if len(buf) + len(para) + 1 <= 900:
            buf = (buf + "\n" + para).strip()
        else:
            if len(buf) >= 60:
                chunks.append({"title": title, "url": url, "text": buf})
            buf = para
    if len(buf) >= 60:
        chunks.append({"title": title, "url": url, "text": buf})
    return chunks


class SiteData:
    def __init__(self):
        self.loaded_at = 0
        self.chunks = []      # [{title, url, text}]
        self.products = []    # [{name, price, url, cats, desc}]
        self.categories = []  # [{name, url, count, parent}]

    def refresh(self, force=False):
        if not force and time.time() - self.loaded_at < TTL and self.chunks:
            return
        chunks, products, categories = [], [], []
        try:
            for page in _get("/wp-json/wp/v2/pages", {"per_page": 100, "_fields": "title,link,content,slug"}):
                body = clean_text(page.get("content", {}).get("rendered", ""))
                if body:
                    chunks += chunk_text(body, html.unescape(page.get("title", {}).get("rendered", "")), page.get("link", ""))
        except Exception:
            pass
        try:
            for post in _get("/wp-json/wp/v2/posts", {"per_page": 50, "_fields": "title,link,content"}):
                body = clean_text(post.get("content", {}).get("rendered", ""))
                if body:
                    chunks += chunk_text(body, html.unescape(post.get("title", {}).get("rendered", "")), post.get("link", ""))
        except Exception:
            pass
        try:
            for p in _get("/wp-json/wc/store/v1/products", {"per_page": 100}):
                price = (p.get("prices") or {}).get("price", "")
                try:
                    price = f"{int(price) / 100:.2f}" if price else ""
                except (TypeError, ValueError):
                    price = ""
                products.append({
                    "name": html.unescape(p.get("name", "")),
                    "price": price,
                    "url": p.get("permalink", ""),
                    "cats": [html.unescape(c.get("name", "")) for c in p.get("categories", [])],
                    "desc": clean_text(p.get("short_description", ""))[:300],
                })
        except Exception:
            pass
        try:
            for c in _get("/wp-json/wc/store/v1/products/categories", {"per_page": 100, "hide_empty": "false"}):
                categories.append({"name": html.unescape(c.get("name", "")), "url": c.get("permalink", ""),
                                     "count": c.get("count", 0), "parent": c.get("parent", 0)})
        except Exception:
            pass
        if chunks:
            self.chunks = chunks
        if products:
            self.products = products
        if categories:
            self.categories = categories
        self.loaded_at = time.time()


DATA = SiteData()
