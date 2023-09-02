import re
from typing import List


class MyClass(object):
    def __init__(self):
        pass

    # Задание 1
    def process_number(self, string: str) -> str:
        # Паттерн для поиска особенных номеров
        pattern = r'(\d{2,4})\\(\d{2,5})'

        # Заменяем особенные номера на хорошие номера с помощью лямбда-функции
        processed_string = re.sub(pattern, lambda match: match.group(
            1).rjust(4, '0') + '\\' + match.group(2).rjust(5, '0'), string)

        return processed_string

    # Задание 2
    def add_atms(self, n: int, k: int, distances: List[int]) -> List[int]:
        # Создаем список новых расстояний
        new_distances = []

        # Добавляем сначала существующие расстояния
        for distance in distances:
            new_distances.append(distance)

        # Добавляем новые банкоматы между существующими
        for i in range(k):
            # Берем самое большое расстояние
            max_distance = max(new_distances)
            # Индекс самого большого расстояния
            max_distance_index = new_distances.index(max_distance)
            # Новое расстояние будет половиной максимального
            new_distance = max_distance // 2
            # Вставляем новое расстояние перед максимальным
            new_distances.insert(max_distance_index, new_distance)
            # Вставляем еще одно новое расстояние
            new_distances.insert(max_distance_index + 1, new_distance)
            # Удаляем старое максимальное расстояние
            new_distances.remove(max_distance)

        return new_distances

    # Задание 3
    def max_concatenated_num(self, nums: List[str]) -> str:
        # Сортируем строки в обратном лексикографическом порядке
        sorted_nums = sorted(nums, reverse=True)

        # Конкатенируем отсортированные строки и возвращаем результат
        max_num = ''.join(sorted_nums)

        return max_num


if __name__ == '__main__':
    my_class = MyClass()
    print(my_class.process_number('17\\234'))
    print()

    print(my_class.add_atms(5, 3, [100, 180, 50, 60, 150]))
    print()

    print(my_class.max_concatenated_num(['11', '234', '005', '89']))
    print()
