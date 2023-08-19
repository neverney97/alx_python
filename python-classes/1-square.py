"""
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
You are not allowed to import any module.
"""

class Square:
    """
    This class represents a square.

    It has a private instance attribute, size. The size must always be an integer otherwise a TypeError exception
    with the message "size must be an integer" will be raised.

    if size is less than 0:
        raise a ValueError exception with the message, "size must be >= 0"
    """
    def __init__(self, size=0):
        if not isinstance:
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
