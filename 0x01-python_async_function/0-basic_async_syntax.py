#!/usr/bin env python3
""" A file performing async task"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ a function that recieves a random int and delays for
    a randomly generated time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
