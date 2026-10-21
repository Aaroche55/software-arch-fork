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
