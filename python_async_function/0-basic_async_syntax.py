#!/usr/bin/env python3
"""Basic Function"""
import asyncio
import random


async def wait_random(max_wait=10):
    """Wait for a random number of seconds"""
    wait = random.uniform(0, max_wait)
    await asyncio.sleep(wait)
    return wait
