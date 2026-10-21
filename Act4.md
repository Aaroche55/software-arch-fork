# Activity 4: Country Comparison

## What was added
- **analysis.py**: `country_stats_for_period()` gives the count, total and average for one country (start and end years included). `compare_countries()` runs that for both countries and picks the leader, or `None` for a tie. Both reuse the existing `_total_hours()` helper.
- **data_prep.py**: `find_unknown_countries()` checks the countries the user typed against the data. `parse_year_range()` turns the year inputs into ints, or returns `None` if they aren't numbers or start is after end. Input checking lives here because data_prep is the validation layer.
- **presentation.py**: `ask_comparison()`, `show_comparison()` and `show_error()`.
- **main.py**: `run_comparison()` connects all of the above and shows an error instead of crashing when a country is unknown or the years are bad.

## Architectural changes
None were needed. The new feature fit into the existing modules without adding any new ones or changing any existing functions. `data_loader.py` wasn't touched at all, and the existing country, year and graph features still give the same output.
