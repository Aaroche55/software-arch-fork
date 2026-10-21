import analysis
import presentation
from data_loader import load_eva_data
from data_prep import find_unknown_countries, parse_year_range, prepare_records

DATA_FILE = "eva-data.json"
GRAPH_FILE = "cumulative_duration.png"


def run_comparison(evas):
    country_a, country_b, start_text, end_text = presentation.ask_comparison()

    unknown = find_unknown_countries(evas, country_a, country_b)
    if unknown:
        presentation.show_error(f"unknown country: {', '.join(unknown)}")
        return

    year_range = parse_year_range(start_text, end_text)
    if year_range is None:
        presentation.show_error("invalid year range, years must be numbers with start <= end")
        return

    start_year, end_year = year_range
    stats_a, stats_b, leader = analysis.compare_countries(evas, country_a, country_b, start_year, end_year)
    presentation.show_comparison(country_a, country_b, start_year, end_year, stats_a, stats_b, leader)


def main():
    evas = prepare_records(load_eva_data(DATA_FILE))

    country = presentation.ask_country()
    presentation.show_country_total(country, analysis.total_hours_for_country(evas, country))

    year = presentation.ask_year()
    count, hours = analysis.stats_for_year(evas, year)
    presentation.show_year_stats(year, count, hours)

    run_comparison(evas)

    dates, totals = analysis.cumulative_hours(evas)
    presentation.plot_cumulative(dates, totals, GRAPH_FILE)


if __name__ == "__main__":
    main()
