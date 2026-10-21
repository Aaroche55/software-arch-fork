import analysis
import presentation
from data_loader import load_eva_data
from data_prep import prepare_records

DATA_FILE = "eva-data.json"
GRAPH_FILE = "cumulative_duration.png"


def main():
    evas = prepare_records(load_eva_data(DATA_FILE))

    country = presentation.ask_country()
    presentation.show_country_total(country, analysis.total_hours_for_country(evas, country))

    year = presentation.ask_year()
    count, hours = analysis.stats_for_year(evas, year)
    presentation.show_year_stats(year, count, hours)

    dates, totals = analysis.cumulative_hours(evas)
    presentation.plot_cumulative(dates, totals, GRAPH_FILE)


if __name__ == "__main__":
    main()
