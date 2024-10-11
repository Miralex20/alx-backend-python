#!/usr/bin/env python3
""" An annotated function"""


def safely_get_value(dct, key, default = None):
    """A test function to be annotated"""
    if key in dct:
        return dct[key]
    else:
        return default