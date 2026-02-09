import asyncio


# task 1
async def task1() -> None:
    print("Task 1 started")
    await asyncio.sleep(4)  # taking 4 sec. to complete
    print("Task 1 completed")


# task 2
async def task2() -> None:
    print("Task 2 started")
    await asyncio.sleep(1)  # taking 1 sec. to complete
    print("Task 2 completed")


async def main() -> None:
    await asyncio.gather(task1(), task2())  # both tasks run togather


if __name__ == "__main__":
    asyncio.run(main())
