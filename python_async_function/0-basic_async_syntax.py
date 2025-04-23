#!/usr/bin/env python3
"""
Module fonction affichage nb aléatoire
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Retourne le nb alétoire avec du délai
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
