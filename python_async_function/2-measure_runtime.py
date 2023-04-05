#!/usr/bin/env python3
"""Concurrent coroutines"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure time"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    totalTime = time.perf_counter() - start
    return totalTime
