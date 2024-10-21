"""Testing factory fixtures for the application."""

import os
import csv
import json

import pytest


@pytest.fixture(scope="module")
def dir_path():
    """Return the path to the file."""
    return "data/"


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


def test_file_path(dir_path, process_data):
    """Test the file path."""
    assert dir_path == "data/"

    # Remove the file from the directory path to raise an error.
    try:
        os.remove("data/file_not_found.txt")
    except OSError:
        pass

    # Test the file path raises an error if the file is not found.
    with pytest.raises(FileNotFoundError):
        process_data("file_not_found.txt")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
