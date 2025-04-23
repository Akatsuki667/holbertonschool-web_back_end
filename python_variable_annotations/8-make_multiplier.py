#!/usr/bin/env python3
"""
Module fonction multiplication avec multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Fonction de multiplication d'un float avec un multiplier
    """
    def mul(x: float) -> float:
        return x * multiplier
    return mul
