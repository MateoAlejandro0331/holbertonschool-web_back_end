#!/usr/bin/env python3
"""Basic Function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random number of seconds"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
