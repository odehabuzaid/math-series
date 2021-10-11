from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == "0.1.0"


def test_fibonacci0():
    assert fibonacci(0) == 0

def test_fibonacci1():
    assert fibonacci(1) == 1

def test_fibonacci2():
    assert fibonacci(2) == 1

def test_fibonacci3():
    assert fibonacci(3) == 2



# def test_lucas(n: int):
#     if n == 0:
#         assert lucas(n) == 2
#     elif n == 1:
#         assert lucas(n) == 1
#     elif n == 2:
#         assert lucas(n) == 3
#     elif n == 3:
#         assert lucas(n) == 4
#     elif n == 4:
#         assert lucas(n) == 7
#     elif n == 5:
#         assert lucas(n) == 11
#     elif n == 6:
#         assert lucas(n) == 18


# def test_sum_series(n: int, f: int = 1, s: int = 2):
#     if f == 1 and s == 2:
#         assert sum_series(n) == fibonacci(n)
#     elif f == 2 and s == 1:
#         assert sum_series(n) == lucas(n)
