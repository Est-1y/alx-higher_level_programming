#!/usr/bin/python3

"""
Square Moldule
this create class Square that inherits from `9-Rectangle`.
An Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size):
        """ an initalizer.
        Args
           size: size of side of square
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
