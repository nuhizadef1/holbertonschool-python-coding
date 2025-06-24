#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # private instance attribute
