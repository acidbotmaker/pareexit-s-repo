# Async Function

### What is asyncio?
- `asyncio` is a library to write concurrent code using the async/await syntax.
- It is a high-level structured network code.
---

### What is async function?
- The `async` keyword declares a function as asynchronous, allowing use of await inside it.
- Asynchronous functions run within an event loop (for example using `asyncio.run()`).

```
import asyncio

async def work():
  await asyncio.sleep(0)
  print("Done!")

asyncio.run(work())
```
---

### What is await keyword?
- The `await` keyword pauses execution in an `async` function until the awaited object returns a result.
- `await` can only be used inside functions declared with `async`.

```
import asyncio

async def greet():
  return "Hi"

async def main():
  msg = await greet()
  print(msg)

asyncio.run(main())
```
--- 