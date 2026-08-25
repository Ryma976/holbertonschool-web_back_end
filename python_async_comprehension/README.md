# Python - Async Comprehension

This project covers asynchronous generators and async comprehensions in Python using `asyncio`.

## Tasks Summary

| File | Description |
| --- | --- |
| `0-async_generator.py` | Asynchronous generator coroutine that yields 10 random numbers between 0 and 10 after 1-second delays. |
| `1-async_comprehension.py` | Async coroutine `async_comprehension` that collects 10 random numbers using async comprehension over `async_generator`. |
| `2-measure_runtime.py` | Async coroutine `measure_runtime` that executes `async_comprehension` 4 times concurrently using `asyncio.gather` and measures total runtime. |
