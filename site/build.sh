#!/usr/bin/env bash
# Build the new site into site/public and bundle the previous site under /legacy/.
set -euo pipefail
cd "$(dirname "$0")"
BASEURL="${1:-}"
rm -rf public
python3 tools/conference_uploads.py
if [ -n "$BASEURL" ]; then hugo --minify --baseURL "$BASEURL"; else hugo --minify; fi
mkdir -p public/legacy
( cd .. && git ls-files -z -- . ':!site' ':!.github' ':!CLAUDE.md' ':!conference_papers' | xargs -0 -I{} cp --parents {} site/public/legacy/ )
echo "built: $(find public -name '*.html' | wc -l) html pages"
