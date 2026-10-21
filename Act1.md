# Activity 1: Initial Architectural Assessment

## What it does
Running `evacodev2.py` loads `eva-data.json`, asks you for a country and prints that country's total EVA hours, then asks for a year and prints how many EVAs happened that year and their total hours. After that it saves and shows a graph of cumulative EVA hours over time. Looking at the git history, each new feature just got added to the bottom of the same script.

## Modules and responsibilities
There's only one module, `evacodev2.py`, and it does everything:
- loads the JSON data
- converts durations (`duration_to_hours()`, the only function)
- calculates the totals by country and by year, plus the cumulative graph data
- asks for user input and prints the results
- draws and saves the graph

## Mixed responsibilities
- Each feature asks for input, does the calculation and prints the result all in one block.
- Every feature loops over the raw data again and has its own rules for skipping bad records. That's why the country totals include EVAs with no date but the graph and year totals leave them out, so the numbers don't line up.
- Everything runs at the top level, so just importing the file kicks off the prompts, the prints and the graph.

## Dependencies
- Every feature uses the global `eva_data` and relies on the raw JSON format (key names, `"H:MM"` durations, date strings).
- The graph doesn't use either input, but it still has to wait until both questions are answered.
- matplotlib is needed but isn't listed anywhere, and the file paths only work if you run it from the repo folder.

## Hard to test
- The country and year totals can't be called with test data and don't return anything, because they read from `input()` and a global and then just print.
- The plotting always writes the image file and opens a window.
- The only thing you can test on its own is `duration_to_hours()`.
