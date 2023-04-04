#!/usr/bin/python3
"""
Module prints text with two newlines after
character - . ? :
"""


def text_indentation(text):
    """
    function to print text and two newlines
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError('text must be a string')
    string = "".join([a if a not in ".?:" else a + "\n\n" for a in text])
    print("\n".join([x.strip() for x in string.split("\n")]), end="")
