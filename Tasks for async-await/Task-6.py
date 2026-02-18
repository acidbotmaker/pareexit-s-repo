# Task-6: Create a program that runs async function (in thread) and normal function then waits for thread to finish
import asyncio
import threading
import time
from typing import Callable, Coroutine, Any


# running async functon in thread
def async_in_thread(
    async_func: Callable[[], Coroutine[Any, Any, None]], *args: Any, **kwargs: Any
) -> None:
    asyncio.run(async_func(*args, **kwargs))  # creates new event loop for thread


# async function without params
async def async_task() -> None:
    print("async_task started...")
    await asyncio.sleep(2)
    print("async_task (async thread) done!")


# async function with params
async def async_task_params(name: str, delay: float) -> None:
    print(f"{name} started (delay={delay})...")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} sec!")


# normal function
def normal_task() -> None:
    print("normal_task started...")
    time.sleep(1)
    print("normal_task (main) done!")


def main() -> None:
    # thread to run the async function
    thread1 = threading.Thread(target=async_in_thread, args=(async_task,))
    thread2 = threading.Thread(
        target=async_in_thread, args=(async_task_params, "async_param_task", 3)
    )

    thread1.start()
    thread2.start()

    time.sleep(0.1)
    normal_task()

    thread1.join()
    thread2.join()

    print("All tasks completed!")


if __name__ == "__main__":
    main()
