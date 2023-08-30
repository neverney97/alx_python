"""
Write an empty class BaseGeometry.

You are not allowed to import any module
"""

class BaseGeometry:
    """
    The name of the class is as above and it is empty for now.
    """
    def __dir__(cls):
        """
        This is a method to remove __init_subclass__ from the dir list.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass']
