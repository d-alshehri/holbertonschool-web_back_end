#!/usr/bin/env python3
"""A coroutine that waits for a random delay and returns the delay."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay (included), and returns it."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
