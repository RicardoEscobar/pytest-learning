"""
Test parametrize
"""
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

# Run the test
if __name__ == '__main__':
    pytest.main([__file__])
