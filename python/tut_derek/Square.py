import sys
import math
import random
import threading
import time

# ----- CLASSES OBJECTS -----
# Classes are blueprints for creating objects
# Real world objects have
# attributes : height, weight
# capabilities : run, eat


class Square:

    # init is used to set values for each Square
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    # self is used to refer to an object that
    # we don't possess a name for
    @property
    def height(self):
        print("retrieving the height")
        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):
        # We protect the height from receiving
        # a bad value
        if value.isdigit():
            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # This is the getter
    # self is used to refer to an object that
    # we don't possess a name for
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            # Put a __ before this private field
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)
    
# Create a Square object
square = Square()
square.height = "10"
square.width = "10"
print("Area", square.get_area())