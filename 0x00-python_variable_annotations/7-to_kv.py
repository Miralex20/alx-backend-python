#!/usr/bin/env python3
""" A type annotated function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that returns a tuple with
    the given sting and the float square"""
    return k, v*v
