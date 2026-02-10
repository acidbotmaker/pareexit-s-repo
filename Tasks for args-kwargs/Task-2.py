# Task 2 — Average calculator (*args)
def average(*args: tuple[int, ...]) -> float | None:
    if len(args) == 0:
        return "None"
    return sum(args) / len(args)


print(average(1, 2, 3, 4))
print(average(6))
print(average())
