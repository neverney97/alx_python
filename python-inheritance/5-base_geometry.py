"""
Write a class BaseGeometry (based on 3-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
"""
from typing import Any


class BaseGeometry:
    """
    This is the class' name and it has 2 public instance methods.
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    