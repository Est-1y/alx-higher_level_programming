#!/usr/bin/python3

# AUTHOR - Esther

class Base:
    '''Representation of a base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
