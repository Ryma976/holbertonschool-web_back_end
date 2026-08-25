#!/usr/bin/env python3
"""Module for task 1: Let's execute multiple coroutines at the same time."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return delays in order."""
    delays: List[float] = []
    tasks: List[asyncio.Task] = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
