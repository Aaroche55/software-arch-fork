from data_prep import EVA


def _total_hours(evas):
    total = 0
    for eva in evas:
        total += eva.hours
    return total


def total_hours_for_country(evas: list[EVA], country):
    return _total_hours(eva for eva in evas if eva.country == country)


def stats_for_year(evas: list[EVA], year):
    """Number of EVAs and their total hours for a given year"""
    in_year = [eva for eva in evas if eva.date and str(eva.date.year) == year]
    return len(in_year), _total_hours(in_year)


def country_stats_for_period(evas: list[EVA], country, start_year, end_year):
    """Count, total hours and average hours for a country"""
    matching = [
        eva for eva in evas
        if eva.country == country and eva.date and start_year <= eva.date.year <= end_year
    ]
    count = len(matching)
    total = _total_hours(matching)
    average = total / count if count else None
    return count, total, average


def compare_countries(evas: list[EVA], country_a, country_b, start_year, end_year):
    """Stats for both countries plus the one with more total hours"""
    stats_a = country_stats_for_period(evas, country_a, start_year, end_year)
    stats_b = country_stats_for_period(evas, country_b, start_year, end_year)

    if stats_a[1] > stats_b[1]:
        leader = country_a
    elif stats_b[1] > stats_a[1]:
        leader = country_b
    else:
        leader = None

    return stats_a, stats_b, leader


def cumulative_hours(evas: list[EVA]):
    """Dates and running total of EVA hours, in date order."""
    dated = sorted((eva for eva in evas if eva.date), key=lambda eva: eva.date)

    dates = []
    totals = []
    total_hours = 0

    for eva in dated:
        total_hours += eva.hours
        dates.append(eva.date)
        totals.append(total_hours)

    return dates, totals
