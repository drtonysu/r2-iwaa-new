# R2-IWAA — new preview site

Static clinic website for R2 International Wellness & Anti-Aging.

## How this site is built

All page templates and copy live in **`build.py`**. Running it regenerates every HTML file in the repo:

```bash
python3 build.py
```

## Auto-deploy pipeline

Vercel is connected to this GitHub repo. On every push to `main`:

1. Vercel runs `npm run build`, which runs `python3 build.py`
2. `build.py` regenerates all HTML files
3. Vercel publishes the whole folder as a static site

Live URL: https://r2-iwaa-new.vercel.app

## Editing on GitHub

- **Copy or structural changes** → edit `build.py` and commit. HTML regenerates on deploy.
- **Styling** → edit `css/style.css` directly. Not regenerated.
- **Images** → drop new files into `img/` and reference them from `build.py`.

You can edit the pre-built HTML files directly for quick tests, but the next `build.py` run will overwrite them, so put real changes into `build.py`.

## Files

- `build.py` — page templates and copy (edit this)
- `css/style.css` — all styling
- `js/site.js` — nav toggle, scroll reveal, consultation form
- `img/` — photography and generated visuals
- `vercel.json` + `package.json` — deploy configuration
- `*.html` — generated pages (do not edit directly)
