import json


def load_eva_data(path):
    """Read the raw EVA records from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
