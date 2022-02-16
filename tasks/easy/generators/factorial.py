"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    number = 1
    for i in range(1, 5):
        number *= i
        yield number


# def factorial():
#     current = 1
#     result = 1
#     while True:
#         result *= current
#         yield result
#         current += 1
