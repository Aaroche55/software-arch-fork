from dataclasses import dataclass
from datetime import datetime


@dataclass
class EVA:
    country: str
    date: datetime | None
    hours: float


def duration_to_hours(duration_text):
    hours, minutes = map(int, duration_text.split(":"))
    return hours + minutes / 60


def find_unknown_countries(evas, *countries):
    """Return any of the given countries that don't appear in the data."""
    known = {eva.country for eva in evas}
    return [country for country in countries if country not in known]


def parse_year_range(start_text, end_text):
    """Return (start, end) as ints, or None if they aren't valid years or start is after end."""
    try:
        start_year, end_year = int(start_text), int(end_text)
    except ValueError:
        return None
    return (start_year, end_year) if start_year <= end_year else None


def prepare_records(raw_data):
    """Turn raw JSON records into EVAs, skipping any without a duration."""
    evas = []

    for eva in raw_data:
        duration_text = eva.get("duration")
        if not duration_text:
            continue

        date_text = eva.get("date")
        date = datetime.fromisoformat(date_text) if date_text else None
        evas.append(EVA(eva.get("country"), date, duration_to_hours(duration_text)))

    return evas
