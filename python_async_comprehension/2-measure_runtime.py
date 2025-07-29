#!/usr/bin/env python3
"""Measures runtime of running async_comprehension 4 times concurrently."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Run async_comprehension 4 times in parallel and return total runtime."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
