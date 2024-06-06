"""Testing factory fixtures for the application."""
import pytest


@pytest.fixture(scope='function')
def file_path():
    """Return the path to the file."""
    return 'test_data.txt'


@pytest.fixture(scope='function')
def data(file_path):
    """Return the data to be used for testing."""
    def _data(lines_to_read: int = 1):
        with open(file_path, 'r') as file:
            data = file.readlines()[:lines_to_read]
        return data
    
    return _data


def test_file_path(file_path, data):
    """Test the file path."""
    assert file_path == 'test_data.txt'

    # Create a new file
    with open(file_path, 'w') as file:
        for i in range(1, 11, 1):
            file.write(f'Hello {i} times.\n')
    
    # Load the data
    loaded_data = data()
    assert loaded_data == ['Hello 1 times.\n']

    # Load multiple lines
    loaded_data = data(3)
    assert loaded_data == ['Hello 1 times.\n', 'Hello 2 times.\n', 'Hello 3 times.\n']

