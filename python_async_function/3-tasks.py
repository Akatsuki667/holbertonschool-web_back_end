#!/usr/bin/env python3
"""
Module qui crée une tâche asyncio à partir d'une coroutine.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée et retourne une tâche asyncio qui exécute la coroutine wait_random.

    Args:
    max_delay (int): Délai maximum en secondes pour la fonction wait_random.

    Returns:
    asyncio.Task: Une tâche asyncio qui exécute wait_random(max_delay).
    """
    #  Retourne la transformation coroutine wait_random en tâche
    return asyncio.create_task(wait_random(max_delay))
