"""
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""
class Square:
    """
    This class represents a square

    The class has 1 attribute being the size and it is private, as represented using 2 underscores before the attribute name.
    """
    def __init__(self, size=None):
        self.__size = size
