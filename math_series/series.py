def fibonacci(n: int):
    """
    takes n as integer and Returns the nth number in the Fibonacci sequence.
    if the number is less than or equal to 1, return the number.
    if the number is greater than 1, return the nth number in the Fibonacci sequence.
    """
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n: int):
    """
    takes n as integer and Returns the nth number in the Fibonacci sequence.
    if the number is less than or equal to 0, return 2.
    if the number equal or greater than 1, return nth number in the lucas sequence.
    """
    return 2 if n == 0 else fibonacci(n + 1) + fibonacci(n - 1)



def sum_series(n: int, first: int = 0, second: int = 1):
    """
    takes n as integer and Returns :
    nth number in the Fibonacci sequence. if the first argument is 0 and second argument is 1,
    nth number in the lucas sequence. if the first argument is 2 and second argument is 1,
    """
    return fibonacci(n) if first == 0 and second == 1 else lucas(n)
