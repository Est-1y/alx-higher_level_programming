#!/usr/bin/python3

"""
Create class Rectangle that defines a rectangle by
everything from Module 4-rectangle
and expanding that to include:
being able to recognize and print a message if a Rectangle is deleted.
"""


class Rectangle:
    """
    Instantiating variables of width and height

    Args:
        width (int)
        height (int)
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter  # setter method for height
    def height(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of rectangle
        based on valid widths and heights provided.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of rectangle
        based on valid widths and heights given.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print out a rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        """
        as an alternative:
        for k in range(self.__height):
            for z in range(self.__width):
                rectangle_str += "#"
                rectangle_str += "\n"
        return rectangle_str[:-1]
        """
        for x in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """String representation of the rectangle
        to recreate new instance.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Recognize if a rectangle is being deleted
        and print message.
        """
        print("Bye rectangle...")
