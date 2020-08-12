#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geometry import MyPolygon
import pytest

def test_coordinates():
    # Given:
    coordinates = [[0, 0], [0, 2], [2, 2], [2, 0], [0, 0]]
    # test
    assert coordinates == MyPolygon(coordinates).coordinates

def test_valid_list():
    # Given
    coordinates = [("1", 0), ("1", "2"), (2, "2"), ("2", "1"), ("1", "1")]
    with pytest.raises(ValueError):
        MyPolygon(coordinates)
