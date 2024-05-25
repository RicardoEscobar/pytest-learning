"""This module contains the Point class unit tests."""
from code.point import Point
import pytest


def test_make_one_point():
    """Test the creation of a Point object."""
    p1 = Point("Dakar", 14.716677, -17.467686)
    assert p1.get_lat_long() == (14.716677, -17.467686)


def test_invalid_point_generation():
    """Test the creation of a Point object with invalid latitude and longitude."""
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 14.716677, -555.467686)
    assert str(exp.value) == "Invalid latitude or longitude"

if __name__ == "__main__":
    pytest.main()
