#!/usr/bin/env python3
""" A type annotated function"""
from typing import Tuple


def to_kv(k: str, v: float | int) -> Tuple[str, float]:
    return k, v*v
