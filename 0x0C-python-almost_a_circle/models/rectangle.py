#!/usr/bin/python3

# AUTHOR - Esther

'''definition of a rectangle class'''


from models.base import Base

class Rectangle(Base):
    '''Representation of a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        '''an error checking for width'''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

        '''an error checking for height'''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

        '''an error checking for x'''
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

        '''an error checking for y'''
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        '''getter of function for width'''
        return self.__width

    @property
    def height(self):
        '''getter of function for height'''
        return self.__height

    @property
    def x(self):
        '''getter of function for x'''
        return self.__x

    @property
    def y(self):
        '''getter of function for y'''
        return self.__y

    @width.setter
    def width(self, value):
        '''setter of function for width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter of function for height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        '''setter of function for x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        '''setter of function for y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
