def fibonacci(n: int):
    """
    takes n as integer and Returns the nth number in the Fibonacci sequence.
    if the number is less than or equal to 1, return the number.
    if the number is greater than 1, return the sum of the two previous numbers in the sequence.
    """
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n: int):
    """
    takes n as integer and Returns the nth number in the Fibonacci sequence.
    if the number is less than or equal to 0, return 2.
    if the number equal or greater than 1, return the sum of the two previous numbers in the sequence.
    """
    return 2 if n == 0 else fibonacci(n + 1) + fibonacci(n - 1)


print(
    "\n".join([f"{(lucas(i),i)}" for i in range(7)]),
)
print()
print(
    "\n".join([f"{(fibonacci(i),i)}" for i in range(7)]),
)


def sum_series(n: int, first: int = 0, second: int = 1):
    if first == 0 and second == 1:
        return fibonacci(n)
    elif first == 2 and second == 1:
        return lucas(n)
