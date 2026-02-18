# Task-5: Create a program async producer consumer with common queue
import asyncio
from asyncio import Queue


async def producer(q: Queue[int | None], n: int) -> None:
    for item in range(n):
        await q.put(item)  # put item in queue
        print(f"[Producer]: {item}")  # announce production
        await asyncio.sleep(1)  # simulate work (1 sec. delay)
    print(f"[Producer]: Done")
    await q.put(None)


async def consumer(q: Queue[int | None]) -> None:
    while True:
        item = await q.get()  # wait for items from queue
        if item is None:  # check for stop signal
            break
        print(f"[Consumer]: {item}")  # process the item
        await asyncio.sleep(1)  # simulate processing (1 sec.)
    print("[Consumer]: Done")


async def main() -> None:
    n: int = 10
    q: Queue[int | None] = asyncio.Queue()  # shared queue

    # create both tasks
    producer_task = asyncio.create_task(producer(q, n))
    consumer_task = asyncio.create_task(consumer(q))

    # wait for both tasks to finish
    await asyncio.gather(producer_task, consumer_task)


if __name__ == "__main__":
    asyncio.run(main())
