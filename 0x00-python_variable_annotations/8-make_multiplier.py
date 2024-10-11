#!/usr/bin/env python3
''' A type annotated function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ A function maker that creates a muliplier function"""
    def multiplier_function(x: float) -> float:
        """ A function that multiplies a given float
        by an earlier given float"""
        return multiplier * x
    return multiplier_function
