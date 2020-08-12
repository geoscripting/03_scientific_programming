#!/usr/bin/env python
# -*- coding: utf-8 -*-


from geometry import MyPolygon, BaseGeometry


def test_coordinates():
    # Given
    coordinates = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    # When
    my_poly = MyPolygon(coordinates)
    # Then
    assert my_poly.coordinates == coordinates


def test_envelope():
    coordinates = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    base_geometry: BaseGeometry = BaseGeometry(coordinates=coordinates)
    assert [1, 2, 1, 2] == base_geometry.envelope


def test_coordinates_setter_getter_deleter():
    coordinates1 = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    coordinates2 = [(1, 2), (1, 2), (2, 2), (2, 1), (1, 4)]
    base_geometry: BaseGeometry = BaseGeometry(coordinates=coordinates1)
    assert base_geometry.coordinates == coordinates1
    base_geometry.coordinates = coordinates2
    assert base_geometry.coordinates == coordinates2
    del base_geometry.coordinates
    assert base_geometry.coordinates == []
