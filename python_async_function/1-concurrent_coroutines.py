#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """using an async for loop"""
    delays = [wait_random(max_delay) for i in range(n)]
    sort = []
    for await_random in asyncio.as_completed(delays):
        delay = await await_random
        sort.append(delay)
    return sort
