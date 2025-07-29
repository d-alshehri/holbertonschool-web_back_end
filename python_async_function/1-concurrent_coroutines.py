#!/usr/bin/env python3
"""A coroutine that spawns wait_random n times and returns results in order of completion."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times with max_delay, and return list of delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        delays.append(result)

    return delays
