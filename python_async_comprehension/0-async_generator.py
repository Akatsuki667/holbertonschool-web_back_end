#!/usr/bin/env python3
"""
Module fonction générant liste de float.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Générateur asynchrone qui produit 10 nombres flottants aléatoires.
    
    Ce générateur attend 1 seconde entre chaque valeur générée et produit
    un nombre aléatoire entre 0 et 10 (non inclus).
    
    Yields:
    float: Un nombre flottant aléatoire entre 0 et 10.
    
    Returns:
    AsyncGenerator[float, None]: Un générateur asynchrone de nombres flottants.
    """
    for i in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i
