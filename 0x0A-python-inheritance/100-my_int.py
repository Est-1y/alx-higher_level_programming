#!/usr/bin/python3

"""
Module MyInt
Inherit from an int
MyInt is a rebel, MyInt has == and != operators inverted.
"""


class MyInt(int):
    """
    the class utilizing int class that will
    define the class that inverts == !=. operators.
    """

    def __eq__(self, other):
        """an initializer for eq"""
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        """an intializer for greater than"""
        if int.__eq__(self, other):
            return True
        else:
            return False
