import pytest


@pytest.fixture(scope="module")
def dir_path():
    """Return the path to the file."""
    return "data/"