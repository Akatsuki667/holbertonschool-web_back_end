# Python - Async

## 0. The basics of async
- Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.
- Use the `random` module

## 1. Let's execute multiple coroutines at the same time with async
- Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and max_delay. You will spawn `wait_random` n times with the specified `max_delay`.
- `wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.

## 2. Measure the runtime
- From the previous file, import `wait_n` into `2-measure_runtime.py`.
- Create a `measure_time` function with integers`n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.
- Use the `time` module to measure an approximate elapsed time

## 3. Tasks
- Import `wait_random` from `0-basic_async_syntax`.
- Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`
