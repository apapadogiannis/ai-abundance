"""Reads the record of the paper out of its own source, so that nothing in the record is typed.

    python3 -I make_record.py ROOT OUT_DIR

From ROOT/paper/manuscript.tex it writes to OUT_DIR:

    table1.csv         Table 1, one row per actor: the sign of each layer's contribution and the net sign
    table1_signs.csv   the same table, one row per actor and column, with the sign also as a number
    layers.csv         the five layers: name, what the layer holds, and the paper's prediction for it
    claims.csv         the three central claims
    definitions.csv    the paper's own wording of its main terms
    model.csv          Equations 1 to 6, Definition 1, Proposition 1 and its proof

and, from files written for this record and not part of the article:

    symbols.csv        ROOT/data/symbols.csv, after checking that every symbol occurs in the manuscript
    tests.csv          ROOT/beyond/tests.csv, each test joined to the statement or the signs it refers to

Read from the manuscript: every sign, every passage and every equation. Written in this script: which
passages are taken (their first and last words), the identifiers of the rows, the names of the
columns and of the six equations, and the scores that encode the signs.

The script fails if the manuscript does not have the expected shape (24 actors in five panels with
the five layer columns in order, five layers, six numbered equations and no other displayed one) or
if a test refers to something the record does not hold.
Standard library only.
"""
import csv
import os
import re
import sys

ROOT, OUT = sys.argv[1], sys.argv[2]
LAYERS = ["physical", "infrastructural", "capabilities", "institutional", "jurisdictional"]
SCORE = {"++": 2, "+": 1, "0": 0, "-": -1, "--": -2}


def plain(text):
    """LaTeX prose as plain text. Mathematics keeps its LaTeX form, without the delimiters."""
    t = re.sub(r"\s*\\citep?(\[[^\]]*\])*\{[^}]*\}", "", text)       # citations
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\\eqref\{eq:aea_condition\}", "(6)", t)
    t = re.sub(r"\\(emph|textbf|textit|textsc)\{([^{}]*)\}", r"\2", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t)
    t = re.sub(r"\$(.*?)\$", r"\1", t)
    t = t.replace("``", '"').replace("''", '"').replace("~", " ").replace("\\&", "&").replace("\\,", " ")
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r"\s+([.,;:])", r"\1", t)


def between(text, start, end):
    """The one passage of the manuscript that begins with `start` and ends with `end`."""
    i = text.find(start)
    j = text.find(end, i + len(start))
    if i < 0 or j < 0 or text.find(start, i + 1) >= 0:
        raise SystemExit(f"manuscript: passage not found once: {start[:50]!r} ... {end[:30]!r}")
    return text[i:j + len(end)]


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def table1(tex):
    header = re.search(r"& Phys\.\\,\(1\) & Infr\.\\,\(2\) & Cap\.\\,\(3\) & Inst\.\\,\(4\) & Jur\.\\,\(5\) &", tex)
    if not header:
        raise SystemExit("Table 1: the columns are not Phys. (1), Infr. (2), Cap. (3), Inst. (4), Jur. (5), in that order")
    body = between(tex, "\\panel{Panel A:", "\\bottomrule")
    rows, panel, count = [], None, 0
    lines = [l.strip() for l in body.splitlines() if l.strip()]
    for k, line in enumerate(lines):
        m = re.match(r"\\panel\{Panel ([A-E]): (.*)\}$", line)
        if m:
            panel, title, count = m.group(1), m.group(2), 0
            continue
        m = re.match(r"\\pbar & \\textbf\{(.*?)\}(?:\\par\{\\footnotesize \((.*)\)\})?$", line)
        if not m:
            continue
        count += 1
        signs = [c.strip().replace("-{}-", "--") for c in lines[k + 1].rstrip("\\").split("&")[1:]]
        if len(signs) != 6 or any(s not in SCORE for s in signs):
            raise SystemExit(f"Table 1: cannot read the signs of {m.group(1)!r}: {lines[k + 1]}")
        name, note = plain(m.group(1)), plain(m.group(2) or "")
        rows.append([f"{panel}{count}", panel, plain(title), name, note, *signs])
    panels = [sum(r[1] == p for r in rows) for p in "ABCDE"]
    if panels != [7, 4, 7, 2, 4]:
        raise SystemExit(f"Table 1: expected 7, 4, 7, 2 and 4 actors in Panels A to E, found {panels}")
    return rows


def layers(tex):
    listed = between(tex, "\\item \\textbf{Physical layer}", "\\end{enumerate}")
    items = re.findall(r"\\item \\textbf\{(\w+) layer\}: (.*?)(?=\n\s*\\item|\n\\end\{enumerate\})", listed, re.S)
    predictions = re.findall(r"\\subsection\{(?:\\texorpdfstring\{)?Layer (\d): .*?\n(.*?)(?=\n%---|\n\\subsection)", tex, re.S)
    titles = re.findall(r"Layer (\d): (\w+) layer\}", tex)
    if len(items) != 5 or len(predictions) != 5 or [t[1].lower() for t in titles[:5]] != LAYERS or len(set(titles)) != 5:
        raise SystemExit(f"expected five layers, found {len(items)} in the list and {len(predictions)} sections")
    rows = []
    for (name, holds), (number, text) in zip(items, predictions):
        m = re.search(r"Prediction: (.*?\.)(?= [A-Z]|\s*$)", plain(text))
        if not m or name.lower() != LAYERS[int(number) - 1]:
            raise SystemExit(f"layer {number}: name or prediction not found")
        rows.append([number, name.lower(), plain(holds), m.group(1)])
    if len(rows) != 5:
        raise SystemExit(f"expected five layers, found {len(rows)}")
    return rows


def claims(tex):
    listed = between(tex, "\\item \\textbf{ATA does not imply AEA.}", "\\end{enumerate}")
    found = re.findall(r"\\item \\textbf\{(.*?)\} (.*?)(?=\n\s*\\item|\n\\end\{enumerate\})", listed, re.S)
    if len(found) != 3:
        raise SystemExit(f"expected three central claims, found {len(found)}")
    return [[k, plain(title).rstrip("."), plain(text)] for k, (title, text) in enumerate(found, 1)]


DEFINITIONS = [   # term, short name, where it stands, first words, last words
    ("AI technological abundance", "ATA", "Introduction",
     "\\emph{AI technological abundance} (ATA) denotes", "trained, deployed, and scaled."),
    ("AI economic abundance", "AEA", "Introduction",
     "\\emph{AI economic abundance} (AEA) denotes", "owners of scarce bottlenecks."),
    ("binding constraints", "", "Introduction",
     "\\emph{binding constraints} (inputs or permissions", "rising shadow prices)"),
    ("Point A", "", "From cost compression to living standards",
     "We refer to \\emph{Point A} as", "services in the real economy."),
    ("scarcity structure", "", "The structure of scarcity",
     "We define the \\emph{scarcity structure} of an economy as", "at a given point in time."),
    ("post-AI bottlenecks", "", "Introduction",
     "\\emph{post-AI bottlenecks} (layers", "remains binding)"),
    ("institutional and jurisdictional layers", "", "The structure of scarcity",
     "In short, institutions are the rules;", "coercive force and geopolitical weight."),
]


def model(tex):
    rows = []
    equations = re.findall(r"\\begin\{equation\}(.*?)\\end\{equation\}", tex, re.S)
    if len(equations) != 6 or re.search(r"\\begin\{(equation\*|align\*?|gather\*?|multline\*?)\}|\\\[", tex):
        raise SystemExit(f"expected six equations, found {len(equations)}")
    names = ["layer rent vector", "ownership matrix", "rent income of an actor", "disposable resources of a household",
             "price of the reference bundle", "condition for AI economic abundance"]
    for k, (eq, name) in enumerate(zip(equations, names), 1):
        latex = re.sub(r"\s+", " ", re.sub(r"\\label\{[^}]*\}", "", eq)).strip()
        rows.append([f"Equation {k}", name, "latex", latex])
    for env, label in [("definition", "Definition 1"), ("proposition", "Proposition 1"), ("proof", "Proof of Proposition 1")]:
        found = re.findall(r"\\begin\{%s\}(?:\[([^\]]*)\])?(.*?)\\end\{%s\}" % (env, env), tex, re.S)
        if len(found) != 1:
            raise SystemExit(f"expected one {env}, found {len(found)}")
        # The name is the title the article gives in brackets; the proof has none.
        rows.append([label, plain(found[0][0]), "text with LaTeX mathematics", plain(found[0][1])])
    return rows


def main():
    with open(os.path.join(ROOT, "paper", "manuscript.tex"), encoding="utf-8") as f:
        tex = f.read()
    os.makedirs(OUT, exist_ok=True)

    t1 = table1(tex)
    lay = layers(tex)
    write("layers.csv", ["layer", "name", "holds", "prediction"], lay)
    write("claims.csv", ["claim", "title", "text"], claims(tex))
    write("definitions.csv", ["term", "short", "section", "text"],
          [[term, short, where, plain(between(tex, a, b))] for term, short, where, a, b in DEFINITIONS])
    write("model.csv", ["item", "name", "form", "content"], model(tex))

    with open(os.path.join(ROOT, "data", "symbols.csv"), encoding="utf-8", newline="") as f:
        symbols = list(csv.DictReader(f))
    for s in symbols:
        if s["latex"] not in tex:
            raise SystemExit(f"symbols.csv: {s['latex']} does not occur in the manuscript")
    write("symbols.csv", list(symbols[0]), [list(s.values()) for s in symbols])

    signs = {r[0]: r for r in t1}
    central = plain(between(tex, "The post-scarcity narrative presumes that ATA implies AEA.", "it generally does not."))
    with open(os.path.join(ROOT, "beyond", "tests.csv"), encoding="utf-8", newline="") as f:
        tests = list(csv.DictReader(f))
    out, used = [], {}
    for t in tests:
        kind, _, ref = t["refers_to"].partition(":")
        if (kind == "layer" and ref not in {"1", "2", "3", "4", "5"}) or (kind == "table" and not all(x in signs for x in ref.split("<"))) \
                or (kind == "table" and ref.count("<") != 1) or (kind == "claim" and ref != "central"):
            raise SystemExit(f"test {t['id']}: {t['refers_to']} refers to a row, a layer or a claim that the record does not hold")
        if kind == "layer":
            article = "Prediction for layer %s (%s): %s" % (ref, lay[int(ref) - 1][1], lay[int(ref) - 1][3])
        elif kind == "claim":
            article = "Introduction: " + central
        elif kind == "table":
            low, high = ref.split("<")
            for x in (low, high):
                used.setdefault(x, []).append(t["id"])
            if signs[low][-1] not in ("0", "-", "--") or signs[high][-1] not in ("+", "++"):
                raise SystemExit(f"test {t['id']}: the net sign of {low} in Table 1 is not lower than that of {high}")
            article = "Table 1, net sign: %s (%s) %s; %s (%s) %s." % (
                low, signs[low][3], signs[low][-1], high, signs[high][3], signs[high][-1])
        else:
            raise SystemExit(f"test {t['id']}: cannot read refers_to = {t['refers_to']}")
        out.append([t["id"], t["refers_to"], article, *[t[c] for c in list(t)[2:]]])
    write("tests.csv", ["id", "refers_to", "article_says", *list(tests[0])[2:]], out)
    write("table1.csv", ["id", "panel", "panel_title", "actor", "note", *LAYERS, "net", "tests"],
          [[*r, " ".join(used.get(r[0], []))] for r in t1])
    write("table1_signs.csv", ["id", "actor", "column", "layer_number", "sign", "score"],
          [[r[0], r[3], col, "" if col == "net" else k + 1, r[5 + k], SCORE[r[5 + k]]]
           for r in t1 for k, col in enumerate(LAYERS + ["net"])])


if __name__ == "__main__":
    main()