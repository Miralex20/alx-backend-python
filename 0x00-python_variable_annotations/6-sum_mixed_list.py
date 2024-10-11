#!/usr/bin/env python3
""" A type annotated function task"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ A function that takes a mixed list of integers and floats and 
    returns the sum as a float
    """
    return sum(mxd_list)
