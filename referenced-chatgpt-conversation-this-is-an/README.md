# Favour | AI & Technology

A responsive, multi-page portfolio built with plain HTML, CSS and vanilla JavaScript. It is designed for static hosting, including GitHub Pages.

## Preview locally

Open `index.html` in a browser, or start a small local server from this folder:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Pages

- `index.html` — portfolio overview
- `about.html` — background and working principles
- `work/ai-automation/` — AI and workflow automation projects
- `work/product-management/` — product management projects
- `work/project-management/` — project management projects
- `insights.html` — future articles
- `contact.html` — contact links

Each project card opens a structured case study draft with the requested headings. The drafts are marked as placeholders until verified project details are supplied. Do not publish them as completed case studies without replacing their placeholder content.

## Publish with GitHub Pages

1. Create a GitHub repository and add the contents of this folder to its root.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select the default branch and the `/ (root)` folder, then save.
4. Wait for the Pages URL to appear in the Pages settings.

No build step or server-side code is required. Navigation and assets use relative paths so the site works in a GitHub Pages project subdirectory. Google Fonts load over the network; system fallbacks are included.

The optional `scripts/generate_site.py` script creates the initial page set and case study drafts. Edit generated HTML directly for one-off content updates; rerun the script only when you want to regenerate the current template content.

## Project structure

```text
index.html
about.html
insights.html
contact.html
work/
  ai-automation/index.html
  ai-automation/projects/*/index.html
  product-management/index.html
  product-management/projects/*/index.html
  project-management/index.html
  project-management/projects/*/index.html
assets/css/style.css
assets/js/main.js
assets/images/
scripts/generate_site.py  # generator used to create the initial static pages
```

## Content to confirm or add

- Replace case study placeholders with verified project details, evidence, demos and outcomes.
- Add articles after publication.
- CV materials have two details that need reconciliation before they appear as dated/title-specific claims: SASI CRC start date (December 2025 vs January 2026), and Bomcel title (Product Manager vs Project Manager). The LASUTH role should remain **Clinical Research Coordinator**.
- Keep personal workflow builds distinct from paid client deployments. No client outcomes or metrics are currently claimed.

Contact links use the supplied email and LinkedIn profile. No phone number is displayed.
