"""
Write a class BaseGeometry (based on 3-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
"""
class BaseGeometry:
    """
    This is the class' name and it has 1 public instance method.
    """
    def __dir__(cls):
        """
        This is a method to remove __init_subclass__ from the dir list.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        raise Exception("area() is not implemented")