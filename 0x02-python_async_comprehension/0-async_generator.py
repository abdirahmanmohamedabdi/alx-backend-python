#!/usr/bin/env python3
"""" Defines an async generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yields a random number between 0 and 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
