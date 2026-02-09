# Task 7 — Merge dictionaries (**kwargs)
def merge_configs(defaluts: dict[str, any], **overrides: any) -> dict[str, any]:
    return {**defaluts, **overrides}


config = merge_configs({"debug": False}, debug=True, port=8080)
print(config)
