# Task 2 — Average calculator (*args)
def average(*args: int) -> float:
    result = 0
    for x in args:
        result += x / 2
    if result == 0:
        return "None"
    return result


print(average(1, 2))
print(average(6))
print(average())
