# async/await

for using async/await in the code we need to import `asyncio` library first.

Mostly used for handling tasks like network request, database operations or file I/O.

### What is async?
- `async` keyword in Python used to define asynchronous functions, which allow tasks to run without blocking the execution of other code.
- it is basically used for running multiple tasks simultaneously because multiple tasks can run without waiting for one to finish before starting another.
- When called, it returns a coroutine object, which doesn't run on its own but must be scheduled and executed by an **event loop**.
---

### What is await?
- `await` keyword is used only inside an `async def` function to pause the execution of the current coroutine until the awaited result is ready
---

### **Syntax of async/await:**
```
async def function_name():
    await some_async_function()
```

- `async def`: defines an asynchronous function (coroutine function).
- `await`: pauses execution until the awaited function completes.
---

### async with HTTP requests
- If we want to fetch data from the URLs, it is very common pracitce to use `async` with HTTP requests.
- using these we can make program much faster
- for using it we need to import `aiohttp` library first.
- Examples are Task-3.py and Task-4.py files
---

### What is event loop?
- The engine that manages all coroutines, deciding which one to run and when to seitch between them.
- This is the core mechanism that manages and distributes the execution of multiple asynchronous tasks within a single thread.
- When an `await` is encountered, control is returned to the event loop, which can then run other tasks in the meantime.
- The event loop starts via `asyncio.run(main())`
---

### How event loop works?
```
import asyncio

async def greet_after_delay():
    print("Starting...")
    await asyncio.sleep(2)  # Pauses, but doesn't block
    print("Hello!")

asyncio.run(greet_after_delay())
```

Let's understand what happens here:

1. `asyncio.run()` creates an event loop
2. Event loop starts `greet_after_delay()`
3. "Starting..." prints
4. Hits `await asyncio.sleep(2)` -> coroutine pauses
5. Event loop checks: "Any other tasks to run?" (none right now).
6. 2 seconds pass, sleep completes.
7. Event loop resumes `greet_after_delay()`
8. "Hello!" prints.
9. Function finishes -> event loop exits.
---

### What is coroutine (async def)?
- This function defined with `async def` instead of `def`
- It is a special kind of function that can pause its execution and later resume from the same point.
- Scheduling is done by the event loop.
- It must use `await asyncio.sleep(5)` which pauses only that coroutine, not the whole thread.
---