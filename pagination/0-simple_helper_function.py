#!/usr/bin/env python3
"""
Module pour les utilitaires de pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calcule les indices de début et de fin pour la pagination.

    Cette fonction prend en paramètre un numéro de page et une taille de page
    et retourne un tuple contenant les indices de début et de fin correspondant
    à la plage d'éléments à afficher sur la page spécifiée.

    Args:
    page (int): Le numéro de la page actuelle (indexé à partir de 1)
    page_size (int): Le nombre d'éléments par page

    Returns:
    Tuple[int, int]: Un tuple contenant (indice_debut, indice_fin)
    - indice_debut: L'indice du premier élément de la page demandée
    - indice_fin: L'indice du dernier élément de la page demandée + 1

    Exemple:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(2, 10)
        (10, 20)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_idx = (page - 1) * page_size
    end_idx = (page * page_size)
    return (start_idx, end_idx)
