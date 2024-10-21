import csv
import json
import os

import pytest


@pytest.fixture(scope="module")
def process_data(dir_path):
    """Return the data to be used for testing."""
    files = os.listdir(dir_path)

    def _specify_type(filename_or_type: str):
        for file in files:
            if filename_or_type in file:
                if filename_or_type.endswith(".txt"):
                    with open(f"{dir_path}{file}", "r") as file:
                        return file.readlines()
                elif filename_or_type.endswith(".csv"):
                    with open(f"{dir_path}{file}", "r") as file:
                        return list(csv.reader(file))
                elif filename_or_type.endswith(".json"):
                    with open(f"{dir_path}{file}", "r") as file:
                        return json.load(file)
        raise FileNotFoundError(f"File {filename_or_type} not found.")

    return _specify_type
