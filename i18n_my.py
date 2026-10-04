# Myanmar (Burmese) language layer for R2-IWAA.
#
# build.py generates the English pages first. This module then:
#   1. adds an English / Myanmar language switch to every English page, and
#   2. writes a Myanmar copy of every page into /my/, translating each piece of
#      text through the dictionary in i18n/my.json.
#
# To correct a Myanmar translation: open i18n/my.json, find the English text
# (left side) and edit the Myanmar text (right side). Commit, and Vercel rebuilds.
# Any English text that has no entry yet simply stays in English on /my/ pages.
import glob
import json
import os
import re

INLINE = {"em", "strong", "b", "i", "br", "sup", "sub", "small"}
TOK = re.compile(r"(<!--.*?-->|<[^>]+>)", re.S)
TEXT_ATTRS = ("alt", "aria-label", "title", "placeholder")
META_TRANSLATE = ('name="description"', 'property="og:title"', 'property="og:description"')
LETTER = re.compile(r"[A-Za-z]")

MY_FONT = (
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Myanmar:wght@300;400;500;600'
    '&family=Noto+Serif+Myanmar:wght@400;500;600&display=swap" rel="stylesheet">'
)


def _tagname(tok):
    m = re.match(r"</?\s*([a-zA-Z0-9]+)", tok)
    return m.group(1).lower() if m else None


def _clean(slug):
    """index.html -> '' ; iv-therapy.html -> 'iv-therapy' (Vercel cleanUrls)."""
    base = slug[:-5] if slug.endswith(".html") else slug
    return "" if base == "index" else base


def _en_url(slug):
    return "/" + _clean(slug)


def _my_url(slug):
    c = _clean(slug)
    return "/my" + ("/" + c if c else "")


def _switch(slug, lang):
    if lang == "en":
        return (f'<a class="lang-switch" href="{_my_url(slug)}" hreflang="my" lang="my" '
                f'aria-label="မြန်မာဘာသာဖြင့် ကြည့်ရန်">မြန်မာ</a>')
    return (f'<a class="lang-switch" href="{_en_url(slug)}" hreflang="en" lang="en" '
            f'aria-label="View in English">English</a>')


def _alternates(slug):
    return (f'<link rel="alternate" hreflang="en" href="{_en_url(slug)}">\n'
            f'  <link rel="alternate" hreflang="my" href="{_my_url(slug)}">\n'
            f'  <link rel="alternate" hreflang="x-default" href="{_en_url(slug)}">')


def _insert_switch(html, slug, lang):
    if 'class="lang-switch"' in html:
        return html
    sw = _switch(slug, lang)
    # inside the main nav, just before the Consultation button
    html = re.sub(r'(<nav class="nav"[^>]*>.*?)(\s*<a class="btn")',
                  lambda m: m.group(1) + "\n      " + sw + m.group(2), html, count=1, flags=re.S)
    html = html.replace("</head>", f"  {_alternates(slug)}\n</head>", 1)
    return html


def _rewrite_url(url, pages):
    if not url or url.startswith(("#", "/", "http:", "https:", "mailto:", "tel:", "data:", "//", "javascript:")):
        return url
    m = re.match(r"([^#?]*)(.*)", url, re.S)
    path, rest = m.group(1), m.group(2)
    if path in pages:
        return _my_url(path) + rest
    return "/" + url  # shared assets: img/, css/, js/


def _translate_attrs(tok, d, missing, pages):
    def tr_attr(m):
        name, val = m.group(1), m.group(2)
        if name in TEXT_ATTRS and LETTER.search(val):
            if val in d:
                val = d[val]
            else:
                missing.add(val)
        elif name in ("href", "src"):
            val = _rewrite_url(val, pages)
        elif name == "srcset":
            val = ", ".join(" ".join([_rewrite_url(p.split()[0], pages)] + p.split()[1:])
                            for p in val.split(",") if p.strip())
        return f' {name}="{val}"'

    tok = re.sub(r'\s([a-zA-Z-]+)="([^"]*)"', tr_attr, tok)
    if tok.lower().startswith("<meta") and any(k in tok for k in META_TRANSLATE):
        def tr_content(m):
            v = m.group(1)
            if v in d:
                return f'content="{d[v]}"'
            missing.add(v)
            return m.group(0)
        tok = re.sub(r'content="([^"]*)"', tr_content, tok)
    return tok


def translate_html(html, d, pages, missing):
    parts = TOK.split(html)
    out, run = [], []
    skip = None

    def flush():
        if not run:
            return
        s = "".join(run)
        core = s.strip()
        if core and LETTER.search(re.sub(r"<[^>]+>|&[a-zA-Z#0-9]+;", "", core)):
            if core in d:
                lead = s[: len(s) - len(s.lstrip())]
                trail = s[len(s.rstrip()):]
                s = lead + d[core] + trail
            else:
                missing.add(core)
        out.append(s)
        run.clear()

    for p in parts:
        if not p:
            continue
        if p.startswith("<"):
            n = _tagname(p)
            if skip:
                out.append(p)
                if p.startswith("</") and n == skip:
                    skip = None
                continue
            if n in INLINE:
                run.append(p)
                continue
            flush()
            if not p.startswith("<!"):
                p = _translate_attrs(p, d, missing, pages)
            out.append(p)
            if n in ("script", "style", "svg") and not p.startswith("</") and not p.endswith("/>"):
                skip = n
        else:
            if skip:
                out.append(p)
            else:
                run.append(p)
    flush()
    return "".join(out)


def build_all(out_dir):
    dict_path = os.path.join(out_dir, "i18n", "my.json")
    with open(dict_path, encoding="utf-8") as f:
        d = json.load(f)
    pages = {os.path.basename(p) for p in glob.glob(os.path.join(out_dir, "*.html"))}
    my_dir = os.path.join(out_dir, "my")
    os.makedirs(my_dir, exist_ok=True)
    missing = set()
    for slug in sorted(pages):
        path = os.path.join(out_dir, slug)
        with open(path, encoding="utf-8") as f:
            en = f.read()
        en = _insert_switch(en, slug, "en")
        with open(path, "w", encoding="utf-8") as f:
            f.write(en)

        my = en.replace(_switch(slug, "en"), _switch(slug, "my"))
        my = translate_html(my, d, pages, missing)
        my = my.replace('<html lang="en"', '<html lang="my"', 1)
        my = my.replace("</head>", f"  {MY_FONT}\n</head>", 1)
        with open(os.path.join(my_dir, slug), "w", encoding="utf-8") as f:
            f.write(my)
    print(f"Myanmar: {len(pages)} pages written to /my/ ({len(missing)} untranslated strings kept in English)")
    if missing:
        with open(os.path.join(out_dir, "i18n", "my-missing.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(sorted(missing)) + "\n")
