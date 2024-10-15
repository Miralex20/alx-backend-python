#!/usr/bin/env python3
""" A module implementing Measuring the runtime of async function"""
import time
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Calculates the average time of wait_n"""
    start = time.time()
    task = asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start/n

n = 5
max_delay = 9

print(measure_time(n, max_delay))