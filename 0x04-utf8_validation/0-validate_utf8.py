#!/usr/bin/python3
"""
validating whether data is utf-8 valid
"""
import codecs


def validUTF8(data):
    """
    data -> a list containing int values
    RETURN: Boolean
    """
    if data:
        try:
            bytes_data = bytes(data)
            decoded_data = codecs.decode(bytes_data, 'utf-8')
            if decoded_data:
                return True
        except Exception:
            return False
    else:
        return 'exepected data argument'
