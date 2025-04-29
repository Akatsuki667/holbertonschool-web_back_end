#!/usr/bin/env python3
"""
Module pour les utilitaires de pagination
"""
import csv
import math
from typing import Tuple, List
index_range = __import__('0-simple_helper_function').index_range


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

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Récupère une page spécifique du dataset.

        Args:
            page (int, optionnel): Le numéro de la page à récupérer (indexé à partir de 1).
            Par défaut, la première page.
            page_size (int, optionnel): Le nombre d'éléments par page.
            Par défaut, 10 éléments.

        Returns:
        List[List]: Une liste contenant les éléments de la page demandée.
        Retourne une liste vide si:
        - Le dataset est vide
        - La page demandée est hors limites

        Raises:
            AssertionError: Si page n'est pas un entier positif
            Si page_size n'est pas un entier positif
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        if not dataset:
            return []
        
        #  Calcul indices de début et de fin pour la page demandée
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        #  Slicing pour extraction élément dataset
        return dataset[start_index:end_index]
