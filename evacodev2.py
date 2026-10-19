import json
from datetime import datetime
import matplotlib.pyplot as plt


def duration_to_hours(duration_text):
    """Convert a duration string like '2:30' into hours as a float."""
    hours, minutes = map(int, duration_text.split(":"))
    return hours + minutes / 60


with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")

    if not date_text or not duration_text:
        continue

    date = datetime.fromisoformat(date_text)
    duration_hours = duration_to_hours(duration_text)
    records.append((date, duration_hours))

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

for date, duration_hours in records:
    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)

# Ask the user which country to summarise (countries in the data: USA, Russia)
selected_country = input("Enter a country (USA or Russia): ").strip()

total_hours_per_country = 0

for eva in eva_data:
    duration_text = eva.get("duration")
    if not duration_text:
        continue

    if eva.get("country") == selected_country:
        total_hours_per_country += duration_to_hours(duration_text)

print(f"Total EVA hours for {selected_country} is: {total_hours_per_country}")

# Ask for a year and report EVA count and total duration for that year
selected_year = input("Enter a year: ").strip()

total_eva_in_year = 0
total_hours_per_year = 0

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")

    if not date_text or not duration_text:
        continue

    if date_text[:4] != selected_year:
        continue

    total_eva_in_year += 1
    total_hours_per_year += duration_to_hours(duration_text)

print(f"Total EVAs in {selected_year} was: {total_eva_in_year}")
print(f"Total duration of EVAs in {selected_year} was: {total_hours_per_year}")

# Graph of cumulative EVA hours over years
plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
