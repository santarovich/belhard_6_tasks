"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n: int) -> int:
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    check_number(n // 2)
    return True


# def check_number(n: int) -> int:
#     if n == 0:
#         return False
#     while n != 1:
#         if n % 2 != 0:
#             return False
#         n = n // 2
#     return True


# print(check_number(16))
