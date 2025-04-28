#!/usr/bin/env python3
"""
Module qui démontre l'utilisation des compréhensions asynchrones en Python.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires en utilisant une compréhension asynchrone.

    Cette fonction utilise une compréhension de liste asynchrone pour collecter
    10 nombres flottants aléatoires générés par async_generator.

    Returns:
    List[float]: Une liste contenant 10 nombres flottants aléatoires.
    """
    #  async for: itération générateur asynchrone
    #  Pour chaque valeur async_generator, la valeur est ajouté à la liste
    result = [value async for value in async_generator()]
    return result
