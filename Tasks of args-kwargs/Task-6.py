# Task 6 — Wrapper function (real-world use)
def call_function(func: callable, *args: any, **kwargs: any) -> any:
    return func(*args, **kwargs)


print(call_function(max, 1, 5, 3))
call_function(print, "Hello", end="!\n")
