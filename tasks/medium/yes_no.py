"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(collection: list[int]) -> None:
    for number, element in enumerate(collection):
        if element in collection[:number]:
            print('Yes')
        else:
            print('No')


# print(*('Yes' if j in collection[:i] else 'No' for i, j in enumerate(collection)), sep='\n', end='')


# print(yes_or_no([1, 2, 3, 2, 5, 6, 1, 7]))
