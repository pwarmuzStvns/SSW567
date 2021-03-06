"""
Created on Thu Jan 14 13:44:00 2016
Original buggyTriangle created by:
@author: jrr

This file is the fixed version of the buggyTriangle file that was previously created.
The reason for two files is to leave the buggyTriangle file intact for testing and
only modify the other file to ensure testing results are consistent as people work on the project.
"""

import unittest
import test_cases

MAX_INPUT_VALUE = 200


def classifyTriangle(a, b, c, precision=2):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
    """
    # Attempt to convert input variables to floats
    try:
        a, b, c, = float(a), float(b), float(c)
    except ValueError:
        return 'InvalidInput'

    # Check if input values are too big
    if a > MAX_INPUT_VALUE or b > MAX_INPUT_VALUE or c > MAX_INPUT_VALUE:
        return 'InvalidInput'

    # Check if input values are too small
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Triangle inequality
    # The sum of the lengths of any two sides must be greater than or equal to the length of the remaining side.
    if (a + b < c) or (a + c < b) or (b + c < a):
        return 'NotATriangle'

    if a == b and a == c and b == c:
        return 'Equilateral Triangle'

    if a ** 2 + b ** 2 == round(c ** 2, precision) or a ** 2 + c ** 2 == round(b ** 2, precision) or b ** 2 + c ** 2 == round(a ** 2, precision):
        return "Right Isosceles Triangle" if a == b or b == c or a == c else "Right Scalene Triangle"
    return "Isosceles Triangle" if a == b or b == c or a == c else "Scalene Triangle"

if __name__ == "__main__":
    """ Run the Unit tests found in test_cases.py """
    suite = unittest.TestLoader().loadTestsFromTestCase(test_cases.TestTrianglesFixed)
    unittest.TextTestRunner(verbosity=2).run(suite)
