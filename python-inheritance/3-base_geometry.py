"""
Write an empty class BaseGeometry.

You are not allowed to import any module
"""

from collections.abc import Iterable


class BaseMetaClass(type):
    """
    The class above represents a meta class for removing __init_subclass__ from the main class, BaseGeometry.
    """
    def __dir__(cls):
        """
        Method to remove __init_subclass__
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=BaseMetaClass):
    """
    The name of the class is as above and it is empty for now.
    """
    def __dir__(BaseGeometry):
        """
        This is a method to remove __init_subclass__ from the dir list.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
print(dir(BaseGeometry))
