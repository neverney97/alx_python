"""
Write the class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height - this super call will use the logic of the __init__ of the Rectangle class. The width and height must be assigned to the value of size
You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.
"""

from models.rectangle import Rectangle
""" This is an import module for importing the Rectangle class from the rectange file"""

class Square(Rectangle):
    """This class, Square, inherits from its superclass Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ This is the __init__ method"""
        super().__init__(width, height, x, y, id=None)
        self.__height = size
        self.__width = size
        self.__size = size
        self.__x = x
        self.y = y
    
    def __str__(self):
        """This method overrides the method in the rectange superclass"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))

