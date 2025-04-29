#!/usr/bin/env python3
"""
Module mesure le temps d'exécution de tâches asynchrones.
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure temps d'exécution pour quatre appels à async_comprehension.

    Returns:
    float: Le temps total d'exécution en secondes.
    """
    start = perf_counter()
    #  Création 4 appels async_comprehension()
    #  * unpacks l'expression génératrice que appel = argument
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = perf_counter()
    return end - start
