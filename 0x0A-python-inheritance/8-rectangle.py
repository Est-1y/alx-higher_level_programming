#!/usr/bin/python3

"""
Module for based on `7-base_geometry`
An Instantiation with width and height: def __init__(self, width, height):
the width and height must be private. No getter or setter
the width and height must be positive integers, validated by integer_validator
It creates a clas rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class rectangle extends from Base Geometry
    """
    def __init__(self, width, height):
        """
        an initializer.
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
