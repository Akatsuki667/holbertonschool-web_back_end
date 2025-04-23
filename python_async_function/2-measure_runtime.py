#!/usr/bin/env python3
"""
Module qui définit une fonction pour mesurer le temps d'exécution moyen
de la fonction wait_n.
"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution total pour wait_n(n, max_delay) et retourne
    le temps d'exécution moyen par opération.

    Args:
    n (int): Nombre de fois que wait_random sera appelé dans wait_n.
    max_delay (int): Délai maximum possible en secondes pour chaque attente.

    Returns:
    float: Temps d'exécution total divisé par n (temps moyen par opération).
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()
    return (end - start) / n
