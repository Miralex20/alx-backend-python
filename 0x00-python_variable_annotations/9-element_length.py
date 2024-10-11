#!/usr/bin/env python3
"""An annotated function"""
from typing import List, Sequence, Tuple


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """ A function that returns a tuple"""
    return [(i, len(i)) for i in lst]