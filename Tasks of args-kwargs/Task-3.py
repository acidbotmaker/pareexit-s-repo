# Task 3 — Flexible logger (**kwargs)
def log_event(**kwargs: any) -> None:
    for key, val in kwargs.items():
        print(f"{key}={val}")


log_event(user="alice", action="login", ip="1.2.3.4")
