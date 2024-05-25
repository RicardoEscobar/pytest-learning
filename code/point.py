"""This module contains the Point class."""


class Point:
    """A point on the Earth's surface."""

    def __init__(self, name, lattitude, longitude):
        if not isinstance(name, str):
            raise ValueError(f"Invalid city name. Must be a string and not of type: {type(name)}")

        self.name = name

        if not (-90 <= lattitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude or longitude")

        self.lattitude = lattitude
        self.longitude = longitude

    def get_lat_long(self):
        return (self.lattitude, self.longitude)
