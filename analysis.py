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
