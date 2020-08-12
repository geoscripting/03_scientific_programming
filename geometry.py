#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseGeometry(object):
    """
    Base geometry class sharing methods to child classes.
    """

    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    @property
    def coordinates(self) -> list:
        """
        Property getter for coordinates. Can be overwritten by child classes.
        """
        return self._coordinates if not None else list()

    @coordinates.setter
    def coordinates(self, coordinates: list):
        """
        Property setter for coordinates. Should be overwritten from child classes.
        """
        self._coordinates = coordinates

    @coordinates.deleter
    def coordinates(self):
        self._coordinates = []

    @property
    def envelope(self) -> list:
        """
        Return the envelope or bounding box of the geometry.
        """
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        for coordinate in self.coordinates:
            if coordinate[0] < min_x:
                min_x = coordinate[0]
            if coordinate[1] < min_y:
                min_y = coordinate[1]
            if coordinate[0] > max_x:
                max_x = coordinate[0]
            if coordinate[1] > max_y:
                max_y = coordinate[1]
        return [min_x, max_x, min_y, max_y]


class MyPolygon:

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def envelope(self):
        # paste your code here
        pass