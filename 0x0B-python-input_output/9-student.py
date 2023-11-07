#!/usr/bin/python3
"""
the class Student
"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """this Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """thisreturns a presentation of a Student instance"""
        return self.__dict__
