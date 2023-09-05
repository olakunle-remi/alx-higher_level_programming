#!/usr/bin/python3
"""Defines a Rectangle class."""
class Rectangle:
    """ rectangle class created"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
		two inter argument width and height
            width (int): width of  rectangle.
            height: height of rectangle  """
        self.width = width
        self.height = height

    @property """applying a decorator  """
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
