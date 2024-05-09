#!/usr/bin/env python3
"""
Defines an Async Generator
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, each time asynchronously
    wait 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
