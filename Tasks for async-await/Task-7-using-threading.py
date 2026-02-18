# Task-7: Write a program that uses multiple event loop to run different async functions
import asyncio
import threading
from typing import List, Tuple


async def async_task(name: str, duration: float) -> None:
    print(f"[Thread {threading.get_ident()}] Task {name} starting...")
    await asyncio.sleep(duration)
    print(f"[Thread {threading.get_ident()}] Task {name} finished after {duration}s.")


def run_in_loop(tasks: List[Tuple[str, float]]) -> None:
    loop = asyncio.new_event_loop()  # create new event loop
    asyncio.set_event_loop(loop)  # current thread's loop

    try:
        # coroutine, inside the process that will run them
        coroutines = [async_task(name, dur) for name, dur in tasks]
        loop.run_until_complete(asyncio.gather(*coroutines))  # run async function
    finally:
        loop.close()


def main() -> None:
    # define tasks for both tasks
    p1_tasks = [("A", 2), ("B", 1)]
    p2_tasks = [("C", 3), ("D", 1)]

    # different threads using seperate event loops
    thread1 = threading.Thread(target=run_in_loop, args=(p1_tasks,))
    thread2 = threading.Thread(target=run_in_loop, args=(p2_tasks,))

    print("Starting thread...")
    thread1.start()  # start thread1
    thread2.start()  # start thread2

    thread1.join()  # wait for first thread to finish
    thread2.join()  # wait for second thread to finish

    print("All threads have completed!")


if __name__ == "__main__":
    main()
