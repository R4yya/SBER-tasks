from timeit import timeit
import random
import string

# Случайные массивы строк для сортировки
# Массив строк фиксированной длины
nums_fixed_length = [''.join(random.choices(string.digits, k=1))
                     for _ in range(10000)]
# Массив строк разной длины
nums_variable_length = [''.join(random.choices(
    string.digits, k=random.randint(1, 10))) for _ in range(10000)]


def max_concatenated_num(nums):
    # Сортируем строки в обратном лексикографическом порядке
    sorted_nums = sorted(nums, reverse=True)

    # Конкатенируем отсортированные строки и возвращаем результат
    max_num = ''.join(sorted_nums)

    return sorted_nums


def radix_sort(nums):
    # Определяем максимальное количество разрядов
    max_length = len(max(nums, key=len))

    # Запускаем сортировку для каждого разряда справа налево
    for i in range(max_length - 1, -1, -1):
        # Создаем 10 корзин для каждой цифры (0-9)
        buckets = [[] for _ in range(10)]

        # Распределяем элементы по корзинам на основе текущего разряда
        for num in nums:
            # Если длина числа меньше текущего разряда, добавляем его в корзину 0
            if len(num) <= i:
                buckets[0].append(num)
            else:
                digit = int(num[i])
                buckets[digit].append(num)

        # Собираем элементы обратно в список
        nums = []
        for bucket in buckets:
            nums.extend(bucket)

    # Объединяем отсортированные строки в одну строку (в обратном порядке)
    sorted_str = ''.join(nums[::-1])

    return nums[::-1]


def radix_sort_wrapper():
    return radix_sort(nums_variable_length)


def sorted_wrapper():
    return max_concatenated_num(nums_variable_length)


if __name__ == '__main__':
    # Замер времени выполнения радикс-сортировки
    # 100 повторений
    radix_time = timeit(radix_sort_wrapper, number=100)
    print(f"radix: {radix_time} sec")
    # print(radix_sort_wrapper())

    # Замер времени выполнения сортировки с использованием sorted
    # 100 повторений
    sorted_time = timeit(sorted_wrapper, number=100)
    print(f"sorted: {sorted_time} sec")
    # print(sorted_wrapper())
