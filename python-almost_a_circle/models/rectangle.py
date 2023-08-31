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
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Contructor method


        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    
    @property
    def width(self):
        """ Getter for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    
    @property
    def height(self):
        """getter for height"""
        return self.__height
    
    
    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """ Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """ Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This is a function for determining the area of a rectangle"""
        return self.height * self.width
    
    def display(self):
        """ This method prints in the stdout the Rectangle instance with the charcter #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    
    def __str__(self):
        """ This method returns something"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
    

