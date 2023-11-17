#!/usr/bin/python3

# AUTHOR - Esther Akinyi

'''
testing class Rectangle
'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''represention of testing classes and methods'''

    # testing for valid initializations.

    def test_initialization(self):
        '''0. testing initialization of height and width'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        '''1. testing the superclass id'''
        r1_id = r1.id
        self.assertEqual(r1_id, 1)

        '''2. testing the initialization again to test id'''
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        '''3. testing the superclass id'''
        r2_id = r2.id
        self.assertEqual(r2_id, 2)

        '''4. testing initialization including x and y'''
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        '''5. testing superclass id'''
        r3_id = r3.id
        self.assertEqual(r3_id, 12)

    # testing for values

    def test_invalid_width_init(self):
        '''testing initialization of non-int width'''
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle('4', 12)

        error_msg = 'width must be an integer'
        self.assertEqual(str(e.exception), error_msg)

    def test_invalid_width_init_0(self):
        '''testing initialization of non-int width'''
        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(0, 12)

        error_msg = 'width must be > 0'
        self.assertEqual(str(e.exception), error_msg)

    def test_invalid_height_init(self):
        '''testing initialization of non-int height'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(2, 'invalid')

        error_msg = 'height must be an integer'
        self.assertEqual(str(e.exception), error_msg)

    def test_zero_height_value(self):
        '''testing if height is zero'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(14, 0)

        error_msg = 'height must be > 0'
        self.assertEqual(str(e.exception), error_msg)

    def test_negative_height_value(self):
        '''testing when height has negative value'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(12, -3)

        error_mgs = 'height must be > 0'
        self.assertEqual(str(e.exception), error_mgs)

    def test_x_not_int(self):
        '''testing when x is not integer'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(2, 10, 'x', 1)

        error_msg = 'x must be an integer'
        self.assertEqual(str(e.exception), error_msg)

    def test_y_not_int(self):
        '''testing when y is not integer'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(2, 10, 1, 'y')

        error_msg = 'y must be an integer'
        self.assertEqual(str(e.exception), error_msg)

    def test_neg_x(self):
        '''testing when x is negative'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(2, 10, -1, 1)

        error_msg = 'x must be >= 0'
        self.assertEqual(str(e.exception), error_msg)

    def test_zero_x(self):
        '''testing for if x and y are 0'''
        r = Rectangle(2, 17, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_neg_y(self):
        '''testing when y is negative'''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(2, 10, 1, -1)

        error_msg = 'y must be >= 0'
        self.assertEqual(str(e.exception), error_msg)


    # testing for setting values with valid and invalid values

    # testing for valid input
    def test_set_width(self):
        '''testing setting the width'''
        r1 = Rectangle(2, 10)
        r1.width = 2
        self.assertEqual(r1.width, 2)

    def test_set_height(self):
        '''testing setting the height'''
        r1 = Rectangle(2, 10)
        r1.height = 6
        self.assertEqual(r1.height, 6)

    def test_set_x(self):
        '''testing setting the x'''
        r1 = Rectangle(2, 10, 0, 0)
        r1.x = 6
        self.assertEqual(r1.x, 6)

    def test_set_y(self):
        '''testing setting the y'''
        r1 = Rectangle(5, 12, 1, 1)
        r1.y = 0
        self.assertEqual(r1.y, 0)


    # testing for invalid input  # value error
    def test_set_width_invalid(self):
        '''testing setting invalid width'''
        r = Rectangle(4, 10)
        with self.assertRaises(ValueError) as e:
            r.width = -5
        err_msg = 'width must be > 0'
        self.assertEqual(str(e.exception), err_msg)

    def test_set_height_invalid(self):
        '''testing setting invalid height'''
        r = Rectangle(4, 10)
        with self.assertRaises(ValueError) as e:
            r.height = -5
        err_msg = 'height must be > 0'
        self.assertEqual(str(e.exception), err_msg)

    def test_set_x_invalid(self):
        '''testing setting invalid x'''
        r = Rectangle(4, 10)
        with self.assertRaises(ValueError) as e:
            r.x = -5
        err_msg = 'x must be > 0'
        self.assertEqual(str(e.exception), err_msg)

    def test_set_y_invalid(self):
        '''testing setting invalid y'''
        r = Rectangle(4, 10)
        with self.assertRaises(ValueError) as e:
            r.y = -5
        err_msg = 'y must be >= 0'
        self.assertEqual(str(e.exception), err_msg)


    # testing for invalid input  # type error
    def test_set_width_invalid(self):
        '''testing setting invalid width'''
        r = Rectangle(4, 10)
        with self.assertRaises(TypeError) as e:
            r.width = 'invalid'
        err_msg = 'width must be an integer'
        self.assertEqual(str(e.exception), err_msg)

    def test_set_height_invalid(self):
        '''testing setting invalid height'''
        r = Rectangle(4, 10)
        with self.assertRaises(TypeError) as e:
            r.height = 'invalid'
        err_msg = 'height must be an integer'
        self.assertEqual(str(e.exception), err_msg)

    def test_set_x_invalid(self):
        '''testing setting invalid x'''
        r = Rectangle(4, 10)
        with self.assertRaises(TypeError) as e:
            r.x = 'invalid'
        err_msg = 'x must be an integer'
        self.assertEqual(str(e.exception), err_msg)

    def test_set_y_invalid(self):
        '''testing setting invalid y'''
        r = Rectangle(4, 10)
        with self.assertRaises(TypeError) as e:
            r.y = 'invalid'
        err_msg = 'y must be an integer'
        self.assertEqual(str(e.exception), err_msg)

if __name__ == '__main__':
    unittest.main()
