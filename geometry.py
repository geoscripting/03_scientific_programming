#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyPolygon:

    def __init__(self, coordinates):
        self.coordinates = coordinates
        types = [isinstance(c, str) for pair in self.coordinates for c in pair]
        if True in types:
            raise ValueError

    @property
    def envelope(self):
        coords = np.array(self._coordinates)
        min_x = min(coords[:, 0])
        max_x = max(coords[:, 0])
        min_y = min(coords[:, 1])
        max_y = max(coords[:, 1])
        return ([min_x, min_y, max_x, max_y])