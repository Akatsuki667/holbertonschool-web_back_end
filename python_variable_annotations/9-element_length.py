#!/usr/bin/env python3
"""
Module Annotations de fonction
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Retourne une liste
    """
    return [(i, len(i)) for i in lst]
