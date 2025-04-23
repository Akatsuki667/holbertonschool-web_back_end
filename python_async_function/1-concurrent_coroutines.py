#!/usr/bin/env python3
"""
Module qui implémente une fonction asynchrone wait_n qui exécute
plusieurs coroutines concurrentes et retourne leurs résultats dans
l'ordre de complétion.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute n fois wait_random(max_delay) de façon concurrente
    et retourne les délais dans l'ordre de complétion.

    Args:
    n (int): Nombre de fois à exécuter wait_random.
    max_delay (int): Délai maximum possible (en secondes) pour chaque attente.

    Returns:
        List[float]: Liste des délais d'attente dans l'ordre de complétion.
    """
    list = []
    #  Génération n coroutine
    coroutine = [wait_random(max_delay) for _ in range(n)]
    #  Traitement des résultats dans l'ordre de complétion
    for task in asyncio.as_completed(coroutine):
        #  Pour chaque task terminé:
        #  Attends résultat avec wait
        result = await task
        #  Ajoute à la liste
        list.append(result)
    return list
