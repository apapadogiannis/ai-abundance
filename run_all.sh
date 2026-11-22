#!/usr/bin/env bash
# Rebuilds the record from the manuscript source. Runs in under a second. Standard library only.
set -e
cd "$(dirname "$0")/scripts"
mkdir -p ../outputs
# The table, the layers, the claims, the definitions and the model, read out of paper/manuscript.tex,
# and the tests of the added page (beyond/), joined to the statements and signs they refer to.
echo "== make_record"; python3 -I make_record.py .. ../outputs
# The description of the record tables (outputs/results.json) and the guide for programs and AI
# agents (llms.txt).
# The guide names the Zenodo archive, so it is written from the first release that has one.
if grep -q '^doi:' ../CITATION.cff; then
  echo "== make_guide"; python3 -I make_guide.py
else
  echo "== make_guide: skipped until CITATION.cff carries the archive DOI"
fi
