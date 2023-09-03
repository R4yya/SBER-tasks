import unittest
from main import MyClass


class TestMyClass(unittest.TestCase):

    def setUp(self):
        self.my_class = MyClass()

    # Тесты для задания 1
    def test_extract_good_numbers_with_padding(self):
        input_string = '17\\234'
        expected_output = ['0017\\00234']
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    def test_extract_good_numbers_without_padding(self):
        input_string = '1234\\56789'
        expected_output = ['1234\\56789']
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    def test_extract_good_numbers_first_group(self):
        input_string = '12\\34567'
        expected_output = ['0012\\34567']
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    def test_extract_good_numbers_second_group(self):
        input_string = '1234\\567'
        expected_output = ['1234\\00567']
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    def test_extract_good_numbers_with_text(self):
        input_string = 'Адрес 5467\\456. Номер 405\\549'
        expected_output = ['5467\\00456', '0405\\00549']
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    def test_extract_good_numbers_only_text(self):
        input_string = 'Адрес. Номер'
        expected_output = []
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    def test_extract_good_numbers_empty(self):
        input_string = ''
        expected_output = []
        result = self.my_class.extract_good_numbers(input_string)
        self.assertEqual(result, expected_output)

    # Тесты для задания 2
    def test_add_atms_basic(self):
        n = 5
        k = 3
        distances = [100, 180, 50, 60, 150]
        expected_output = [50, 50, 90, 90, 50, 60, 75, 75]
        result = self.my_class.add_atms(n, k, distances)
        self.assertEqual(result, expected_output)

    def test_add_atms_equal_distances(self):
        n = 3
        k = 2
        distances = [60, 60, 60]
        expected_output = [30, 30, 30, 30, 60]
        result = self.my_class.add_atms(n, k, distances)
        self.assertEqual(result, expected_output)

    def test_add_atms_two_plus_one(self):
        n = 2
        k = 1
        distances = [160]
        expected_output = [80, 80]
        result = self.my_class.add_atms(n, k, distances)
        self.assertEqual(result, expected_output)

    def test_add_atms_no_extra_atms(self):
        n = 5
        k = 0  # Пусть и ноль не натуралоьное число
        distances = [100, 180, 50, 60, 150]
        expected_output = distances
        result = self.my_class.add_atms(n, k, distances)
        self.assertEqual(result, expected_output)

    def test_add_atms_big_distance(self):
        n = 5
        k = 4
        distances = [400, 180, 50, 60, 150]
        expected_output = [100, 100, 100, 100, 90, 90, 50, 60, 150]
        result = self.my_class.add_atms(n, k, distances)
        self.assertEqual(result, expected_output)

    # Тесты для задания 3
    def test_max_concatenated_num_basic(self):
        nums = ['11', '234', '005', '89']
        expected_output = '8923411005'
        result = self.my_class.max_concatenated_num(nums)
        self.assertEqual(result, expected_output)

    def test_max_concatenated_num_single_digit(self):
        nums = ['9', '8', '6', '7']
        expected_output = '9876'
        result = self.my_class.max_concatenated_num(nums)
        self.assertEqual(result, expected_output)

    def test_max_concatenated_num_equal_strings(self):
        nums = ['10', '10', '10']
        expected_output = '101010'
        result = self.my_class.max_concatenated_num(nums)
        self.assertEqual(result, expected_output)

    def test_max_concatenated_num_zeroes(self):
        nums = ['0', '00', '000']
        expected_output = '000000'
        result = self.my_class.max_concatenated_num(nums)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMyClass)
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite)
    total_tests = test_result.testsRun
    total_failures = len(test_result.failures)
    total_errors = len(test_result.errors)
    total_success = total_tests - total_failures - total_errors
    success_percentage = (total_success / total_tests) * 100

    print(f'Total Tests: {total_tests}')
    print(f'Total Success: {total_success}')
    print(f'Total Failures: {total_failures}')
    print(f'Total Errors: {total_errors}')
    print(f'Success Percentage: {success_percentage:.2f}%')

    if total_failures > 0:
        print('\nFailures:')
        for test_case, failure_message in test_result.failures:
            print(f'{test_case.id()}: {failure_message}')

    if total_errors > 0:
        print('\nErrors:')
        for test_case, error_message in test_result.errors:
            print(f'{test_case.id()}: {error_message}')
