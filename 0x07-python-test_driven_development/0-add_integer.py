#!/usr/bin/python3
"""
Module adds two integers and returns sum of two numbers a and b.
Only accepts integers and floats else TypeError is raised
Float is converted to integer before sumation
"""


def add_integer(a, b=98):
    """
    add_integer: Checks input if correct,
    cast both into ints and return the sum
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))
