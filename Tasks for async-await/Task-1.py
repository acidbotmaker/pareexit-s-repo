# Task-1: Sequentially execute two async functions one by one
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


# Sequentially execute functions
async def main() -> None:
    await func_one()
    await func_two()


if __name__ == "__main__":
    asyncio.run(main())
