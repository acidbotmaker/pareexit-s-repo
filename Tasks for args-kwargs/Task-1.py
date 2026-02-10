# Task 1 — Sum any number of numbers (*args)
def sum_all(*args: tuple[int, ...]) -> int:
    result = 0
    for x in args:
        result += x
    return result


print(sum_all(1, 2, 3))
print(sum_all(10))
