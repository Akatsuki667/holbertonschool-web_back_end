#!/usr/bin/env python3
"""
Module fonction de somme d'éléments mixte d'une liste
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Retourne la somme des éléments de la liste en float
    """
    return sum(mxd_lst)
