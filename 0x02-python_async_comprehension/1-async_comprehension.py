#!/usr/bin/env python3
"""
Defines an synchronouse comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random number
    then return 10 random number.
    """
    return [n async for n in async_generator()]
