#!/usr/bin/env python3
"""Collect conference papers uploaded to ../conference_papers into site/data/conference_uploads.json.

Each paper is a PDF and/or a short card (.yaml) with the same file name.
The card is flat "key: value" lines, so no YAML library is needed.
A PDF without a card is still listed, using its file name
(YYYY[-MM[-DD]]_Venue_Title.pdf) for year, venue and title.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'conference_papers')
OUT = os.path.join(HERE, '..', 'data', 'conference_uploads.json')
KEYS = ('authors', 'title', 'venue', 'details', 'year', 'date', 'url')


def read_card(path):
    card = {}
    with open(path, encoding='utf-8-sig') as f:
        for line in f:
            if line.lstrip().startswith('#') or ':' not in line:
                continue
            k, v = line.split(':', 1)
            k = k.strip().lower()
            v = re.sub(r'\s+#.*$', '', v).strip().strip('"').strip("'")
            if k in KEYS and v:
                card[k] = v
    return card


def from_filename(stem):
    m = re.match(r'^(\d{4})(?:[-.](\d{1,2}))?(?:[-.](\d{1,2}))?[_ ]+(.*)$', stem)
    if not m:
        return {'title': stem.replace('_', ' ')}
    y, mo, d, rest = m.groups()
    parts = rest.split('_', 1)
    card = {'year': y, 'title': (parts[1] if len(parts) > 1 else parts[0]).replace('_', ' ')}
    if len(parts) > 1:
        card['venue'] = parts[0].replace('-', ' ')
    if mo:
        card['date'] = '%s-%02d-%02d' % (y, int(mo), int(d or 1))
    return card


def main():
    items = {}
    if os.path.isdir(SRC):
        for name in sorted(os.listdir(SRC)):
            stem, ext = os.path.splitext(name)
            ext = ext.lower()
            if stem.startswith('_') or ext not in ('.pdf', '.yaml', '.yml'):
                continue
            it = items.setdefault(stem, {})
            if ext == '.pdf':
                it['pdf'] = name
            else:
                it['card'] = read_card(os.path.join(SRC, name))
    out = []
    for stem, it in items.items():
        e = dict(from_filename(stem))
        e.update(it.get('card', {}))
        if 'year' not in e and e.get('date'):
            e['year'] = e['date'][:4]
        if not re.fullmatch(r'\d{4}', str(e.get('year', ''))):
            print('conference_papers: skipped %s (no year)' % stem, file=sys.stderr)
            continue
        e['year'] = int(e['year'])
        e.setdefault('details', str(e['year']))
        e.setdefault('date', '%d-00-00' % e['year'])
        if 'pdf' in it:
            e['pdf'] = it['pdf']
        out.append(e)
    out.sort(key=lambda e: e['date'], reverse=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('conference_papers: %d item(s)' % len(out))


if __name__ == '__main__':
    main()
