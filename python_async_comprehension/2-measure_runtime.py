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

    Cette fonction crée 4 tâches asynchrones exécutant async_comprehension,
    les exécute en parallèle avec asyncio.gather() et mesure le temps total
    d'exécution.

    Returns:
    float: Le temps total d'exécution en secondes.
    """
    coroutines = []
    for _ in range(4):
        result = async_comprehension()
        coroutines.append(result)
    start = perf_counter()
    await asyncio.gather(*coroutines)
    end = perf_counter()
    return (end - start)
