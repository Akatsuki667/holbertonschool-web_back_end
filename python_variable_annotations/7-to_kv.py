#!/usr/bin/env python3
"""
Module fonction retournant un tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne tuple
    """
    return (k, v * v)
