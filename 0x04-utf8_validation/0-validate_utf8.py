#!/usr/bin/python3
"""
Module Docs
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data (List[int]): List of integers representing 1-byte data.
    Each integer represents 8 least significant bits.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else return False.
    """
    expected_continuations = 0
    for byte in data:
        if expected_continuations == 0:
            if (byte >> 5) == 0b110:
                expected_continuations = 1
            elif (byte >> 4) == 0b1110:
                expected_continuations = 2
            elif (byte >> 3) == 0b11110:
                expected_continuations = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_continuations -= 1
    return expected_continuations == 0
