# Adnovaa Assistant — website chat bot server (Flask, Render free tier).
#
# Owner rules (2026-10-23):
#  1. ALL answers come from the website's own data (fetched live via WP REST +
#     Woo Store API, 10-min cache) — when the site is updated, answers update.
#  2. The bot answers in the SAME language the visitor asks in (free machine
#     translation layer; falls back to English if translation is unavailable).
#  3. Payment problems, disputes and unknowns go to a human: the website
#     widget collects name/email/issue and emails admin@adnovaa.com instantly.

import json
import os
import re
import unicodedata

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

from fetcher import DATA, SITE
from knowledge import LOCAL, QUICK_REPLIES

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": ["https://adnovaa.com", "https://www.adnovaa.com"]}})

GTX = "https://translate.googleapis.com/translate_a/single"
_tr_cache = {}

STOP = set("the a an and or of to in on for with is are do does how can i you my me it this that "
           "what where when why who be is it at by from as your our their there here have has".split())


def translate(text, tl, sl="en"):
    """Free gtx translation with URL protection + caching. Falls back to source."""
    if not text or tl == sl:
        return text
    key = (sl, tl, text[:200])
    if key in _tr_cache:
        return _tr_cache[key]
    urls = []

    def _hide(m):
        urls.append(m.group(0))
        return f" ⟦{len(urls) - 1}⟧ "

    protected = re.sub(r"https?://[^\s]+", _hide, text)
    out = protected
    try:
        # gtx handles ~1500 chars per call comfortably; split on paragraph bounds
        parts, buf = [], ""
        for para in protected.split("\n"):
            if len(buf) + len(para) > 1400 and buf:
                parts.append(buf)
                buf = para
            else:
                buf = (buf + "\n" + para) if buf else para
        if buf:
            parts.append(buf)
        done = []
        for part in parts:
            r = requests.get(GTX, params={"client": "gtx", "sl": sl, "tl": tl, "dt": "t", "q": part}, timeout=10)
            r.raise_for_status()
            data = json.loads(r.content.decode("utf-8-sig"))
            done.append("".join(seg[0] for seg in data[0] if seg and seg[0]))
        out = "\n".join(done)
        for i, u in enumerate(urls):
            out = out.replace(f"⟦{i}⟧", u)
    except Exception:
        out = text
    _tr_cache[key] = out
    return out


def detect_lang(text):
    for ch in text:
        o = ord(ch)
        if 0x0980 <= o <= 0x09FF:
            return "bn"
        if 0x0900 <= o <= 0x097F:
            return "hi"
        if 0x0400 <= o <= 0x04FF:
            return "ru"
        if 0x0600 <= o <= 0x06FF:
            if any(w in text for w in ("ہوں", "نہیں", "کیا", "آرڈر")):
                return "ur"
            return "ar"
    low = " " + text.lower() + " "
    hints = {
        "es": [" hola ", " gracias ", " comprar ", " cuánto ", " precio ", " pedido "],
        "fr": [" bonjour ", " merci ", " acheter ", " commande ", " prix "],
        "de": [" hallo ", " danke ", " kaufen ", " bestellung ", " preis "],
        "pt": [" olá ", " obrigado ", " comprar ", " pedido ", " preço "],
        "tr": [" merhaba ", " teşekkür ", " satın ", " sipariş ", " fiyat "],
    }
    for lang, words in hints.items():
        if any(w in low for w in words):
            return lang
    return "en"


def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def tokens(s):
    return [t for t in norm(s).split() if len(t) > 2 and t not in STOP]


def wants_human(text, lang):
    t = norm(text)
    if any(norm(w) in t for w in LOCAL[lang]["human_words"]):
        return True
    return any(w in t for w in ["talk to a human", "real person", "customer support", "human handoff"])


PRODUCT_HINTS = ["price", "cost", "buy", "find", "search", "looking for", "show me", "দাম", "कीमत",
                 "precio", "prix", "preis", "цена", "fiyat", "سعر", "কিনতে", "कितना"]


def find_products(query_en):
    qt = set(tokens(query_en))
    if not qt:
        return []
    scored = []
    for p in DATA.products:
        name_t = set(tokens(p["name"]))
        score = len(qt & name_t) * 3 + len(qt & set(tokens(" ".join(p["cats"]))))
        if score >= 3:
            scored.append((score, p))
    scored.sort(key=lambda x: -x[0])
    return [p for _, p in scored[:4]]


def retrieve(query_en):
    """Best-matching chunk of live site content for the query."""
    qt = tokens(query_en)
    if not qt:
        return None
    best, best_score = None, 0
    for ch in DATA.chunks:
        ct = tokens(ch["text"])
        if not ct:
            continue
        score = sum(2 if t in tokens(ch["title"]) else 1 for t in qt if t in ct or t in tokens(ch["title"]))
        if "/faq/" in ch["url"]:
            score = int(score * 1.5)
        if score > best_score:
            best, best_score = ch, score
    # require a meaningful overlap: at least 2 query tokens or 40% of them
    need = max(2, int(len(qt) * 0.4))
    return best if best_score >= need else None


def categories_answer():
    parents = [c for c in DATA.categories if c.get("parent") == 0 and c["name"].lower() != "uncategorized"]
    if not parents:
        return None
    lines = [f"Adnovaa has {len(DATA.categories)} categories. The main groups are:"]
    for c in parents:
        lines.append(f"• {c['name']} — {c['url']}")
    lines.append("Tell me a product name and I'll look it up for you.")
    return "\n".join(lines)


@app.route("/", methods=["GET"])
def home():
    DATA.refresh()
    return jsonify({"status": "Adnovaa Assistant running", "version": "2.0.0",
                    "chunks": len(DATA.chunks), "products": len(DATA.products),
                    "categories": len(DATA.categories)})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True, silent=True) or {}
    msg = str(data.get("message", "")).strip()[:500]
    lang = detect_lang(msg) if msg else "en"
    loc = LOCAL[lang]
    DATA.refresh()

    def respond(en_text, **kw):
        reply = translate(en_text, lang) if lang != "en" else en_text
        quick = [translate(q, lang) for q in QUICK_REPLIES] if lang != "en" else QUICK_REPLIES
        return jsonify({"reply": reply, "quick": quick, "lang": lang, **kw})

    if not msg:
        return jsonify({"reply": loc["greeting"], "quick": QUICK_REPLIES, "lang": "en"})

    if msg.lower().strip("!. ") in ("hi", "hello", "hey", "hola", "bonjour", "hallo",
                                     "merhaba", "হ্যালো", "नमस्ते", "مرحبا", "السلام علیکم",
                                     "здравствуйте", "olá"):
        return jsonify({"reply": loc["greeting"],
                        "quick": [translate(q, lang) for q in QUICK_REPLIES] if lang != "en" else QUICK_REPLIES,
                        "lang": lang})

    if wants_human(msg, lang):
        return jsonify({"reply": loc["handoff"], "handoff": True, "lang": lang})

    # Work in English against the site data; translate the answer back.
    query_en = translate(msg, "en", sl=lang) if lang != "en" else msg
    qn = norm(query_en)

    if "categor" in qn:
        ans = categories_answer()
        if ans:
            return respond(ans)

    if any(h in norm(msg) for h in PRODUCT_HINTS) or any(h in qn for h in PRODUCT_HINTS):
        hits = find_products(query_en)
        if hits:
            lines = ["Here's what I found on Adnovaa:"]
            for p in hits:
                price = f" — {p['price']} USDT" if p["price"] else ""
                lines.append(f"• {p['name']}{price}\n  {p['url']}")
            return respond("\n".join(lines))

    chunk = retrieve(query_en)
    if chunk:
        text = chunk["text"]
        if len(text) > 1100:
            text = text[:1100].rsplit(" ", 1)[0] + "…"
        return respond(f"{text}\n\nMore: {chunk['url']}")

    hits = find_products(query_en)
    if hits:
        lines = ["Here's what I found on Adnovaa:"]
        for p in hits:
            price = f" — {p['price']} USDT" if p["price"] else ""
            lines.append(f"• {p['name']}{price}\n  {p['url']}")
        return respond("\n".join(lines))

    return jsonify({"reply": loc["fallback"], "handoff_offer": True,
                    "quick": [translate(q, lang) for q in QUICK_REPLIES] if lang != "en" else QUICK_REPLIES,
                    "lang": lang})


if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: DATA.refresh(force=True), daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
