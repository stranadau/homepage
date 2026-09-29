# STRANA homepage — update notes

Prof. Hyun Woo Park, Structural Analysis Lab., Dong-A University. Communicate with the owner in Korean.

## Publishing
- Live site: https://stranadau.github.io/homepage/ — the Hugo site in `site/`, built and deployed by `.github/workflows/pages.yml` on every push to `main` (Pages source: "GitHub Actions").
- Develop on a branch, get the owner's review, then fast-forward `main`.
- Rollback: set Settings -> Pages -> Source back to "Deploy from a branch" (`main`, root) to serve the legacy HTML directly.

## Sources of truth when updating
- Publication lists: `publications.htm` (EN) and `publications_kor.htm` (KR) must stay identical in content.
- Google Scholar profile (cross-check new papers, venues, years, DOIs):
  https://scholar.google.com/citations?user=2K8ydwMAAAAJ&hl=ko
  The cloud environment's network policy must allow `scholar.google.com` for this to work.
- Research topics pages cite only representative papers; every cited paper must exist in the publication list with the same DOI and year.

## New site (Hugo, `site/`)
- Source in `site/` (custom theme, no external modules; Hugo 0.123.7). Data-driven: `site/data/*.yaml`, one YAML file per news item in `site/data/news/`.
- The old site is bundled under `/legacy/` by `site/build.sh`. Keep updating the legacy pages together with the Hugo data (owner's decision): every content change goes to both.
- `site/static/*.htm` are redirect stubs so old root URLs keep working: current pages point to the matching new page, archives to `legacy/<same file>`. Add a stub when a new root-level legacy page is created.

## Page map (legacy site)
- Frames: `index.htm` / `index_kor.htm` -> menus `top.htm` / `top_kor.htm` + content frame.
- Front page: `main.htm` / `main_kor.htm`, image `images/main_2026_timeline.png` (source: `.svg` next to it).
- Research topics: `research_topics_2026.htm` / `research_topics_kor_2026.htm` (KR titles: Korean title + English original beneath).
- Older year-suffixed files (e.g. `research_topics_2025.htm`, `publications_2022.htm`) are archives; keep them, but point the menus at the current year.

## Conventions
- Entry format: `Authors, "Title," <i>Journal</i>, Vol., pages/article, year.` with `https://doi.org/` links.
- Author name order: "Nur Indah Mukharromah".
- Contact e-mail: hwpark@dau.ac.kr (written "hwpark at dau.ac.kr" in resume text).
- Resume: `resume.htm` (EN, CP949 bytes) and `resume_kor.htm` (KR, UTF-8); members pages link to them.
- `publications*.htm` and `main.htm` use CRLF line endings; `main.htm` contains CP949 bytes — edit it byte-preserving (e.g. latin-1 round trip).
- When renaming a year-suffixed page, update every menu that links to it.
