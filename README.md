# Scarcity in an age of AI abundance

[![SSRN](https://img.shields.io/badge/SSRN-10.2139%2Fssrn.5924462-1f4e79)](https://doi.org/10.2139/ssrn.5924462)
[![check](https://github.com/apapadogiannis/ai-abundance/actions/workflows/check.yml/badge.svg)](https://github.com/apapadogiannis/ai-abundance/actions/workflows/check.yml)

Record of the paper by Agisilaos Papadogiannis, forthcoming in *Asian Review of Political Economy* (2027), [doi:10.1007/s44216-026-00090-y](https://doi.org/10.1007/s44216-026-00090-y).
Paper: `paper/manuscript.pdf` (author's version of the accepted text, with LaTeX source); preprint on SSRN: [doi:10.2139/ssrn.5924462](https://doi.org/10.2139/ssrn.5924462).

**This is a paper record, not a replication package.** The paper is theoretical: it has no data
and no computation, so there is nothing to reproduce. The record holds what the paper states, in a
form that can be looked up and checked against later evidence.

## For AI agents and programs

*The two files named here are written at version 1.0, once the Zenodo archive has its DOI. Until
then, start at the tables below.*

Read [`llms.txt`](llms.txt) first. It says what the record holds, what it adds over reading the
paper, how to read the signs of the table and what not to use them for.
[`outputs/results.json`](outputs/results.json) describes the eight tables and every column, and
carries the paper, the identifiers, the version, the licence and the citation under its `package`
key. Both files are written by `scripts/make_guide.py` from `CITATION.cff`, `guide.toml` and the
stored tables, and both are covered by the check.

## What this is

The paper asks whether advanced AI and robotics end scarcity. Its answer:

1. **Cheap production is not broad affordability.** AI can make many goods and services cheap to
   produce (AI technological abundance, ATA) without making an essential standard of living
   broadly affordable (AI economic abundance, AEA).
2. **Scarcity moves; it does not vanish.** Binding constraints and their rents shift to five
   layers: physical resources, infrastructure, capabilities, institutions and jurisdictions.
3. **Distribution follows ownership.** Who gains depends on who holds claims on the layers where
   rents rise.

The record holds:

- **Table 1 as data**: 24 actors and industries, with the expected direction of each layer's
  contribution to their rent income. The article calls these entries schematic and conjectural,
  and says they are not forecasts.
- **The five layers**, each with the one-sentence prediction the paper makes for it.
- **The model**: six equations, the definition of AEA, the proposition and its proof.
- **The central claims and definitions**, in the paper's own words.
- **One page that goes beyond the article**: [how this paper could be wrong](beyond/README.md).
  For each prediction it gives a measure, two baselines, two dates and the outcome that would count against the
  paper. The article itself gives none of these. No test has been read against data, and the page
  says where the tests are weak.

## Layout

```
paper/      the manuscript PDF and LaTeX source
outputs/    the record: eight tables (CSV); results.json describes them
beyond/     the page that goes beyond the article, and its tests as written by hand
data/       the glossary of symbols, written by hand
scripts/    make_record.py reads the tables out of the manuscript; make_guide.py writes the guide
llms.txt    guide for AI agents and programs, generated; guide.toml holds its statements
```

## The tables

| File | What it holds | From |
|---|---|---|
| `outputs/table1.csv` | Table 1, one row per actor: five layer signs, the net sign, and which tests use the row | the article; the last column is the record's |
| `outputs/table1_signs.csv` | the same, one row per actor and column, with the sign also as a score | the article |
| `outputs/layers.csv` | the five layers: what each holds and the prediction for it | the article |
| `outputs/claims.csv` | the three central claims | the article |
| `outputs/definitions.csv` | seven terms, each with the passage that defines it | the article |
| `outputs/model.csv` | Equations 1 to 6, Definition 1, Proposition 1 and its proof | the article; the names of the equations are the record's |
| `outputs/symbols.csv` | glossary of 21 symbols | written for this record |
| `outputs/tests.csv` | 11 tests: measure, sources, what counts against the paper | beyond the article |

## Rebuilding the record

Requirements: Python 3.11 or later. No other package is needed.

```bash
./run_all.sh    # under a second
```

| Script | What it produces | Where it comes from |
|---|---|---|
| `make_record.py` | the eight tables in `outputs/` | `paper/manuscript.tex`, `data/symbols.csv`, `beyond/tests.csv` |
| `make_guide.py` | `outputs/results.json` and `llms.txt` | `CITATION.cff`, `guide.toml` and the tables |

`make_record.py` reads the signs, the passages and the equations out of the manuscript source, so
that none of them is typed into the record. What the script supplies is listed at its top: which
passages are taken, the row identifiers, the column names, the names of the equations and the
scores. It fails if the manuscript does not have 24 actors in five panels, the five layer columns
in order, five layers and six equations, if a symbol of the glossary does not occur in the
manuscript, or if a test refers to a row or a layer that does not exist.

## How the check works

```bash
python3 check_outputs.py --also llms.txt    # reruns ./run_all.sh, then compares
```

1. The tables in `outputs/` are stored in this repository.
2. `check_outputs.py` sets the stored copies aside, reruns `./run_all.sh`, and compares the fresh
   files with the stored ones. Text, labels and whole numbers must match exactly.
3. A GitHub Actions workflow does the same on every push and once a month; the badge above shows
   the latest run.

Two limits. The check shows that the record is the one the manuscript source gives. It does not
show that the paper's argument is right. And the comparison is with the manuscript source in
`paper/`, not with the journal's typeset article: the 144 signs of Table 1 were compared with the
table in the journal's proof once, when the record was made, and all agreed. The proof is not in
this repository, so that comparison cannot be repeated from here.

## Licensing

- Paper (`paper/`): CC BY 4.0, the license of *Asian Review of Political Economy*.
- The record (`outputs/`, `data/`, `beyond/`): CC BY 4.0, cite the paper.
- Code: MIT License.

## Citation

> Papadogiannis, A. (2027). "Scarcity in an age of AI abundance." *Asian Review of Political Economy*, forthcoming.
> https://doi.org/10.1007/s44216-026-00090-y
> SSRN: https://doi.org/10.2139/ssrn.5924462

## Disclaimer

Independent research; no funding, no institutional position. Not investment advice.
