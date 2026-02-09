# Task 4 — Student profile builder (**kwargs)
def create_profile(name: str, **kwargs: any) -> dict[str, any]:
    return {"name": name, **kwargs}

print(create_profile("John", age=20, city="NY"))