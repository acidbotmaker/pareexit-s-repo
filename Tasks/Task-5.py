# Task 5 — Price calculator (*args + **kwargs)
def checkout(*prices: float, **options: any) -> float:
    discount = options.get("discount", 0) / 100
    tax = options.get("tax", 0) / 100

    total = 0.0
    for price in prices:
        discount_price = price * (1 - discount)
        total += discount_price * (1 + tax)
    return round(total, 2)


print(checkout(100, 200, discount=10, tax=5))
