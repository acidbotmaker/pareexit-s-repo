# Task-2: Use gather to run multiple tasks at same time
import asyncio


# Task 1
async def func_one() -> None:
    print(f"Started: Function 1")
    await asyncio.sleep(3)
    print(f"Completed: Function 1 (after 3 sec.)")


# Task 2
async def func_two() -> None:
    print(f"Started: Function 2")
    await asyncio.sleep(2)
    print(f"Completed: Function 2 (after 2 sec.)")


# Concurrently execute functions using gather
async def main() -> None:
    await asyncio.gather(func_one(), func_two())


if __name__ == "__main__":
    asyncio.run(main())
