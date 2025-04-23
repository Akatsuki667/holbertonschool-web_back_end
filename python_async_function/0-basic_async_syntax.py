#!/usr/bin/env python3
"""
Module qui définit une fonction asynchrone qui attend un délai aléatoire.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend pendant une durée aléatoire entre 0 et max_delay secondes
    puis retourne cette durée.

    Args:
        max_delay (int, optional): Délai maximum d'attente en secondes.
        Valeur par défaut: 10.

    Returns:
        float: La durée d'attente en secondes.
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
