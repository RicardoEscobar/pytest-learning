"""Testing factory fixtures for the application."""
import os
import csv
import json

import pytest


@pytest.fixture(scope='function')
def dir_path():
    """Return the path to the file."""
    return 'data/'


@pytest.fixture(scope='function')
def process_data(dir_path):
    """Return the data to be used for testing."""
    files = os.listdir(dir_path)

    def _specify_type(filename_or_type: str):
        for file in files:
            if filename_or_type in file:
                if filename_or_type.endswith('.txt'):
                    with open(f'{dir_path}{file}', 'r') as file:
                        return file.readlines()
                elif filename_or_type.endswith('.csv'):
                    with open(f'{dir_path}{file}', 'r') as file:
                        return list(csv.reader(file))
                elif filename_or_type.endswith('.json'):
                    with open(f'{dir_path}{file}', 'r') as file:
                        return json.load(file)
        raise FileNotFoundError(f'File {filename_or_type} not found.')
                
    
    return _specify_type


def test_file_path(dir_path, process_data):
    """Test the file path."""
    assert dir_path == 'test_data.txt'

    # Create a new file
    with open(dir_path, 'w') as file:
        for i in range(1, 11, 1):
            file.write(f'Hello {i} times.\n')
    
    # Load the data
    loaded_data = process_data()
    assert loaded_data == ['Hello 1 times.\n']

    # Load multiple lines
    loaded_data = process_data(3)
    assert loaded_data == ['Hello 1 times.\n', 'Hello 2 times.\n', 'Hello 3 times.\n']
