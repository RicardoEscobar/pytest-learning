"""This module contains the Point class."""


class Point:
    """A point on the Earth's surface."""
    def __init__(self, name, lattitude, longitude):
        self.name = name

        if not (-90 <= lattitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid lattitude or longitude")

        self.lattitude = lattitude
        self.longitude = longitude

    def get_lat_long(self):
        return (self.lattitude, self.longitude)
