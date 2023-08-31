"""
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
"""

from models.base import Base
""" This is an import statement to import the class Base from the base python file
"""

class Rectangle(Base):
    """
    This class represents the rectange class which is a child class of the Base class.


    """
    def __init__(self, width, height, x, y, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """ Getter method for width

    """
    @property
    def width(self):
        return self.__width
    
    """ Setter method for width

    """
    @width.setter
    def width(self, value):
        self.__width = value

    """ getter method for height

    """
    @property
    def height(self):
        return self.__height
    
    """ setter method for height

    """
    @height.setter
    def height(self, value):
        self.__height = value

    """ getter method for x

    """
    def x(self):
        return self.__x
    
    """ Setter method for x

    """
    def x(self, value):
        self.__x = value

    """Getter method for y

    """
    def y(self):
        return self.__y
    
    """setter method for y

    """
    def y(self, value):
        self.__y = value


