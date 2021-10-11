def fibonacci(n: int):
    return (n - 1) + (n - 2)


def lucas(n: int):
    return (n - 1) + (n - 1)


def sum_series(n: int, first: int = 0, second: int = 1):
    if first == 0 and second == 1:
        return fibonacci(n)
    elif first == 2 and second == 1:
        return lucas(n)
