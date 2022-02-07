"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(data: dict, key: str) -> tuple:
    for value in data.values():
        return key, data[key] + 1


def decr_students(data: dict, key: str) -> tuple:
    for value in data.values():
        if value == 0:
            raise ValueError("The number of students in a class cannot be less than 0.")
        return key, data[key] - 1


def add_class(data: dict, key: str) -> dict:
    data.setdefault(key, 0)
    return data


def remove_class(data: dict, key: str) -> dict:
    data.pop(key)
    return data


def calc_students(data: dict) -> int:
    return sum(data.values())
