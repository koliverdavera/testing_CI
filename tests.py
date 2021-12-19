import unittest
from random import randint
from main import *
from functools import reduce
import operator
import time


class TestFunc(unittest.TestCase):
    # тесты для проверки корректности работы программы. Тестовые данные записываются в файл test_data.txt в формате
    # массива, где элементы массива разделены пробелом
    file_name = 'test_data.txt'

    with open(file_name, 'w') as file:
        # генерация тестовых данных в аттрибуте self.data
        data = [randint(1, 1000) for _ in range(randint(1, 10))]
        print(*data, file=file)

    def test_min(self):
        self.assertEqual(min(self.data), find_min(self.data))

    def test_max(self):
        self.assertEqual(max(self.data), find_max(self.data))

    def test_sum(self):
        self.assertEqual(sum(self.data), find_sum(self.data))

    def test_mul(self):
        self.assertEqual(reduce(operator.mul, self.data), find_mul(self.data))


class CheckTime(unittest.TestCase):
    file_name = 'time_testing.txt'
    time_limit = 0.1   # ввод ограничения по времени

    # Нагрузочное тестирование
    def test_check_time(self):
        for i in range(0, 100, 10):
            with self.subTest(i=i):
                # подтесты для проверки работы программы при увеличении входных данных
                param = 'a'
                if i == 0:  # на первом сабтесте файл пересоздается, на последующих тестах данные дозаписываются с
                    # новой строки
                    param = 'w'
                with open(self.file_name, param) as file:  # time_testing.txt - файл для хранения тестовых данных
                    # нагрузочного тестирования. На каждой итерации теста проверяется работа на всех числах файла,
                    # при этом на каждой итерации мы дозаписываем в файл все более длинные массивы
                    lst = [randint(1, 1000) for _ in range(randint(i + 1, (i + 1) * 10))]
                    for numb in lst:
                        file.write(f'{numb} ')
                    file.write('\n')
                start = time.time()
                main('time_testing.txt')
                end = time.time()
                self.assertTrue(end - start < self.time_limit, 'Time limit exceeded')


class TestWrongData(unittest.TestCase):
    # дополнительное тестирование работы программы на некорректных данных
    file_name = 'wrong_data.txt'

    def test_empty_data(self):
        open(self.file_name, 'w').close()   # очистка файла
        # проверка работы программы на пустом файле
        self.assertEqual(main(self.file_name), None, 'Execution on empty file has given non empty result')

    def test_strings_not_numbers(self):
        with open(self.file_name, 'w') as file:
            # запись в файл с данными некорректных значений
            file.write('Some wrong data instead of numbers')
        with self.assertRaises(ValueError):
            # ожидаем ошибку в преобразовании строковых данных к целочисленным
            get_file(self.file_name)


if __name__ == '__main__':
    unittest.main()
