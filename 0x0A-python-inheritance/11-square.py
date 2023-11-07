#!/usr/bin/python3

"""
Square Moldule
This create class Square that inherits from `9-Rectangle`.
(based on 10-square.py)
An Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description:
[Square] <width>/<height>
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size):
        """an initalizer
        Args
           size: size of side of square.
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
        return dimension of square.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
