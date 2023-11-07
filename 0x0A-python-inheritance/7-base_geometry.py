#!/usr/bin/python3

"""
Module for Base Geometry based on `6-base_geometry`
Public instance method: def area(self)
that raises an Exception with the message area() is not implemented
The public instance method: def integer_validator(self, name, value)
that validates value
If value is not integer: raise a TypeError exception
with the message <name> must be an integer.
if value is less or equal to 0: raise a ValueError exception
with the message <name> must be greater than 0
"""


class BaseGeometry:
    """
    A class that estimates the geometry.
    """
    def area(self):
        """
        an unimplemented area function.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        an integer validation.
        Args
           name: name of value
           value: value
        This must be an int greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} this must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} this must be greater than 0".format(name))
