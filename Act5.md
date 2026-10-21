# Activity 5: Verify and Evaluate

## Test evidence
The tests are in `test_analysis.py`. Run them with `python -m unittest -v test_analysis`. All 9 pass.

They use a small hand-made list of EVAs, so the expected answers are easy to work out by hand:
- **Country comparison**: counts, totals, averages and the leader, a tie, start/end years being included, and a country with no EVAs (zero, with the average unavailable).
- **Existing analysis**: `stats_for_year` and `total_hours_for_country`.
- **Invalid input / boundaries**: start year after end year, a non-number year, the same start and end year, and an unknown country.

I also checked the existing features by running the app with the same inputs as in Act 1, and the output was identical (Russia gives 626.58 h, 1985 gives 5 EVAs and 27.23 h).

## Before vs after
- **Modules changed for the new FR:** 4 out of 5 (`analysis`, `data_prep`, `presentation`, `main`), but only by adding new functions. No existing functions were changed and `data_loader` wasn't touched. In the old script it would all have been one more block bolted onto the same file.
- **Dependencies:** `main` uses everything. `analysis` only uses `data_prep` (for the `EVA` type). `data_loader` and `presentation` don't depend on any other module.
- **Testing without files or display:** yes. The tests never read the JSON or print anything. Before, nothing except `duration_to_hours()` could be tested.
- **Responsibilities easier to spot:** yes, because the file name tells you what's inside.
- **Duplication:** reduced. The raw data parsing and the "skip bad records" checks happen once in `data_prep` instead of in every loop, and all the totals go through `_total_hours()`.
- **Unnecessary complexity:** a bit. Five files plus an `EVA` class is a lot for an app this small, but each file is short and easy to follow.

## ADR-002: Test the analysis with hand-made data using unittest

**Context:** We need automated tests with known inputs and expected results.

**Alternatives:** Test against the real `eva-data.json`, run the whole app with fake input and check what it prints, or call the analysis functions directly with a small hand-made list of EVAs.

**Decision:** Call the functions directly with hand-made EVAs, using Python's built-in `unittest`.

**Rationale:** With hand-made data we know the right answers for sure, and they won't change if the JSON file changes. `unittest` comes with Python, so there's no new dependency (pytest would add one). This only works because the restructure split the analysis out from file reading and input/output.

**Consequences:** The tests are fast and simple. The downside is that they don't cover file loading, prompts or the graph, which are still checked by running the app manually.
