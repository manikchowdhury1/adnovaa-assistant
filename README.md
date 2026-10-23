# Adnovaa Assistant

Website chat bot for adnovaa.com. All answers come from the site's own data
(WP REST + Woo Store API, 10-minute cache), answered in the visitor's language
(11 languages, free translation layer with English fallback). Unknowns and
problems go to a human handoff handled on the website side (the WordPress
plugin emails admin@adnovaa.com). Deploy: Render free web service,
build `pip install -r requirements.txt`, start `gunicorn app:app`.
