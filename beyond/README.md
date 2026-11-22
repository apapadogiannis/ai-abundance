# How this paper could be wrong

**This page goes beyond the published article.** The article is theoretical. It states its
predictions without a date and without a measure, and it says of its table that the entries "are
not forecasts". This page adds what the article leaves open: for each prediction, a measure, two
baselines, two dates on which it is read, and the outcome that would count against it. Nothing here was computed.
No reading had been taken when the page was written, on 22 November 2026. The tests are not
blind, however: see the first limit below.

The tests are in [`tests.csv`](tests.csv). The same tests, each joined to the sentence or the signs
of the article it refers to, are in [`../outputs/tests.csv`](../outputs/tests.csv).

## What cannot be tested

**Proposition 1** says that there exist economies in which technological abundance rises and
economic abundance fails. It is proved by constructing one. An existence claim of this kind is true
by construction, and no observation can count against it. The article calls its condition
"falsifiable", and in one sense it is: condition (6) can be checked for a given economy and a given
date, if its terms are measured. That would show whether abundance holds there, not whether the
proposition is true. What can be wrong is the stronger
statement the paper builds on it: that this is the general case, that cost compression does not by
itself reach households, and that rents move to the five layers in the way the paper describes.
The tests below are about those statements.

## The dates

| | Date | Why |
|---|---|---|
| First baseline | 2022, the calendar year | The last full year before general-purpose AI models were in wide public use. It covers the whole period, but most of it had passed when this page was written. |
| Second baseline | 2026, the calendar year | The year in which this page was written. What happens after it could not be seen when the tests were fixed. |
| First reading | data for 2027 | Five years. Early enough to be checked soon, late enough for capacity with long lead times to have been built or not. |
| Final reading | data for 2032 | Ten years from the first baseline, six from the second. The verdict of each test is taken here. |

A measure that swings with the business cycle (tests T7 to T11) is read as an average of three
years ending at the date, at both baselines as well as at the readings. The article names no date itself: its regime boundary, "Point A", is a threshold of
deployment and not a year. The dates are therefore a choice of this page.

## The tests

| Test | Refers to | What would count against the paper, from 2026 to the final reading |
|---|---|---|
| T1 | Prediction for layer 1, physical | Inelastic endowments (urban land, water, critical minerals) became cheaper relative to manufactured goods in most large economies. |
| T2 | Prediction for layer 2, infrastructural | Margins of chip foundries, cloud platforms and data-center operators fell below their baseline although lead times for new capacity had not shortened. |
| T3 | Prediction for layer 3, capabilities | Pay for routine, codifiable work held up or rose relative to pay for frontier work in the same field. |
| T4 | Prediction for layer 4, institutional | In housing, clinical AI and autonomous transport, entry and prices followed AI adoption and not the rules. |
| T5 | Prediction for layer 5, jurisdictional | The share of new AI infrastructure and of high-skilled migration going to high-capacity jurisdictions fell. |
| T6 | The central claim: ATA generally does not imply AEA | The essential bundle took a smaller share of the income of the poorest fifth of households in most economies, without higher transfers and without broader asset holdings. |
| T7 | Table 1: airlines (net 0) against airport slot holders (net +) | Carriers' margins gained relative to those of slot holders and hub operators. |
| T8 | Table 1: mid-market hotels (net -) against prime hotels (net +) | Mid-market margins gained relative to prime locations and strong brands. |
| T9 | Table 1: commoditized shipping (net 0) against integrated logistics (net +) | Carriers' margins gained relative to integrated networks and ports. |
| T10 | Table 1: office trusts (net -) against data-center and logistics trusts (net +) | Office income per unit of floor area gained relative to data centers and logistics property. |
| T11 | Table 1: software product firms (net -) against cloud and AI platforms (net ++) | Margins of software firms without infrastructure gained relative to the platforms. |

The full wording of each measure, the kind of public source it can be read from, the dates, and
what does not count against the paper are in `tests.csv`. The rows of Table 1 that a test uses are
marked in the column `tests` of `../outputs/table1.csv`: 10 of the 24 rows. The other 14, among
them the chip manufacturers, the households and all of Panel B, have no test here.

## How the verdict is taken

- **The verdict is taken on the change from 2026 to 2032.** That is the part of each test that
  was fixed before it could be seen. The change from 2022 is reported beside it. Where the two
  disagree, the reading says so, and the change since 2022 cannot rescue a test that failed since
  2026.

- **The layer predictions** (T1 to T5) are judged one by one. Each stands or falls alone.
- **The central claim** (T6) is the test that matters most. If cost compression alone made the
  essential bundle affordable to the poorest households across most economies, the paper's main
  statement would be wrong in practice, whatever Proposition 1 says in principle.
- **The table** (T7 to T11) is judged as a set. The paper's point is that rents move from the
  commoditized operator to the holder of the scarce complement. T7 to T10 are the article's own
  pairs, a row of Panel C against its counterpart in Panel E. T11 is this page's pairing. If three
  or more of the five contrasts go against the paper, that point has failed.

## Limits of these tests

- **Measured from 2022, the tests are not blind.** The page was written in late 2026, so four of
  the five years to the first reading had already passed. No reading was taken for this page, but
  the direction of several measures over those years is common knowledge, and some of it favours
  the paper (office property, cloud margins). This is why there is a second baseline, 2026, and
  why the verdict is taken from it. The first reading, on data for 2027, is one year after that
  baseline and is weak evidence either way.
- **Direction only.** A test is decided by the sign of a change. No minimum size is set, and no
  series, list of firms or list of countries has been chosen. Whoever takes a reading has to make
  these choices and should state them before looking at the result.
- **Earlier trends.** Some of these measures were already moving the paper's way before 2022, for
  reasons that have nothing to do with AI. A reading should set the change since each baseline
  beside the change over the ten years before 2022.
- **2022 is an unusual base year** for travel, shipping, minerals and property. The three-year
  average softens this for T7 to T11 and does not remove it. The 2026 baseline does not have this
  problem to the same degree.

- **The measures are proxies.** The article defines rents and exposure in the abstract. Margins,
  relative prices and pay ratios are stand-ins, and a different stand-in could give a different
  reading. Each reading should say which series it used.
- **The second test has a way out.** The article's prediction for layer 2 holds "unless capacity
  expands quickly". If capacity does expand quickly and rents fall, the prediction is untested, not
  refuted. The test therefore asks each reading to state whether lead times shortened and how
  much capacity was added.
- **Share prices are not used.** Returns since late 2022 mostly show what investors came to expect.
  The predictions are about rents, so the tests read margins, prices of goods and pay.
- **AI is not the only cause.** Interest rates, energy shocks and trade policy move the same
  measures. A reading that goes the paper's way is consistent with it and does not prove it. A
  reading that goes against it counts against it, because the paper predicts a direction.
- **Only some rows of the table are tested, and only against each other.** A contrast says which of
  two rows did better. It does not test the level the table gives a row: if both rows of a pair
  gain, the test passes although the "-" of one of them was wrong. The single layers within each
  row have no test here.
- **Margins are not rents.** A margin can fall while total rent rises with scale, and the reverse.
