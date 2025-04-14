"""Dummy challenge for Kitt Demo"""
# defining pi
import math
PI = math.pi



def circle_area(radius):
    """Returns the area of the circle of given radius"""


#Scenario 1: radius is negative
    if radius < 0:
        return 0

    return PI * (radius ** 2)
