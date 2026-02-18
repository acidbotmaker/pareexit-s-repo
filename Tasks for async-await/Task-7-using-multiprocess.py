# Task-7: Write a program that uses multiple event loop to run different async functions
import asyncio
import multiprocessing
import os
from typing import List, Coroutine, Any


async def async_task(name: str, duration: float) -> None:
    print(f"[Process {os.getpid()}] Task {name} starting...")
    await asyncio.sleep(duration)
    print(f"[Process {os.getpid()}] Task {name} finished after {duration}s.")


def run_in_loop(tasks: List[Coroutine[Any, Any, None]]) -> None:
    loop = asyncio.new_event_loop()  # create new event loop
    asyncio.set_event_loop(loop)  # current thread's loop

    try:
        # coroutine, inside the process that will run them
        tasks = [async_task(name, dur) for name, dur in tasks]
        loop.run_until_complete(asyncio.gather(*tasks))  # run async function
    finally:
        loop.close()


def main() -> None:
    # define tasks for both processes
    p1_tasks = [("A", 2), ("B", 1)]
    p2_tasks = [("C", 3), ("D", 1)]

    # different threads using seperate event loops
    process1 = multiprocessing.Process(target=run_in_loop, args=(p1_tasks,))
    process2 = multiprocessing.Process(target=run_in_loop, args=(p2_tasks,))

    print("Starting processes...")
    process1.start()  # start thread1
    process2.start()  # start thread2

    process1.join()  # wait for first thread to finish
    process2.join()  # wait for second thread to finish

    print("All processes have completed!")


if __name__ == "__main__":
    main()
