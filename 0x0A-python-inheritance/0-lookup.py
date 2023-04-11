#!/usr/bin/python3
"""
Module contains a function that returns
the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    function returns the list of available attributes,
    method and objects
    """
    return (dir(obj))
