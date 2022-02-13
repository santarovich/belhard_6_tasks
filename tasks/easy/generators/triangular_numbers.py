"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:
Tn = 1 / 2 * n * (n + 1)


Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers():
    for n in range(1, 7):
        number = 0.5 * n * (n + 1)
        yield number
        number += 1


tn_gen = triangular_numbers()
