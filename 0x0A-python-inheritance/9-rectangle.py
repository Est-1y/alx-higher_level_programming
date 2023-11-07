#!/usr/bin/python3

"""
Module for based on `7-base_geometry`
An Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return the following 
rectangle description: [Rectangle] <width>/<height>
It creates a class rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that extends from BaseGeometry(parent class)
    """
    def __init__(self, width, height):
        """
        an initializer
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        the function to return area of a Rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        This returns string of rectangle format.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
