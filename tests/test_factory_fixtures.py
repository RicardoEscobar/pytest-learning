"""Testing factory fixtures for the application."""

import os

import pytest


def test_file_path(dir_path, process_data):
    """Test the file path."""
    assert dir_path == "data/"

    # Remove the file from the directory path to raise an error.
    try:
        os.remove("data/file_not_found.txt")
    except OSError:
        pass

    # Test the file path raises an error if the file is not found.
    with pytest.raises(FileNotFoundError) as error:
        process_data("file_not_found.txt")
    assert str(error.value) == "File file_not_found.txt not found."


if __name__ == "__main__":
    pytest.main(["-v", __file__])
