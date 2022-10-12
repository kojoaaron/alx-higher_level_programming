#!/usr/bin/python3
"""defining a class square"""

class Square:
    """Intialization a new square."""

    def __init__(self, size=0):
        """Intialization a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
            
