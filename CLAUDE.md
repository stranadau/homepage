# STRANA homepage — update notes

Prof. Hyun Woo Park, Structural Analysis Lab., Dong-A University. Communicate with the owner in Korean.

## Publishing
- The live site is served directly from `main`. Develop on a branch, get the owner's review, then fast-forward `main`.

## Sources of truth when updating
- Publication lists: `publications.htm` (EN) and `publications_kor.htm` (KR) must stay identical in content.
- Google Scholar profile (cross-check new papers, venues, years, DOIs):
  https://scholar.google.com/citations?user=2K8ydwMAAAAJ&hl=ko
  The cloud environment's network policy must allow `scholar.google.com` for this to work.
- Research topics pages cite only representative papers; every cited paper must exist in the publication list with the same DOI and year.

## Page map
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
