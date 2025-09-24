
import pytest
from lab2 import fibonacci, bubble_sort, sieve_of_eratosthenes

class TestFibonacci:

    # Позитив тесты
    def test_fibonacci_base_cases(self):
        """Тестирование базовых случаев (n=0, n=1, n=2)."""
        assert fibonacci(0) == []    # Граничное значение
        assert fibonacci(1) == [0]   # Граничное значение
        assert fibonacci(2) == [0, 1]

    def test_fibonacci_positive(self):
        """Тестирование на стандартных валидных данных."""
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(10)[-1] == 34  # Проверка только 10 элемента

    #Негативные тесты
    def test_fibonacci_negative_n(self):
        """Тестирование реакции на отрицательное n."""
        with pytest.raises(ValueError):
            fibonacci(-1) # Граничное значение (отриц. число)
        with pytest.raises(ValueError):
            fibonacci(-10)

    def test_fibonacci_invalid_type(self):
        """Тестирование реакции на нецелый тип данных."""
        with pytest.raises(TypeError):
            fibonacci(5.5) # Дробное число
        with pytest.raises(TypeError):
            fibonacci("5") # Строка

class TestBubbleSort:

    # Позитив
    def test_bubble_sort_standard(self):
        """Тестирование сортировки стандартного списка."""
        input_list = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert bubble_sort(input_list) == expected
        # сверяем с исходником
        assert input_list == [64, 34, 25, 12, 22, 11, 90]

    def test_bubble_sort_already_sorted(self):
        """Тестирование сортировки уже отсортированного списка."""
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_bubble_sort_empty(self):
        """Тестирование сортировки пустого списка (граничное значение)."""
        assert bubble_sort([]) == []

    def test_bubble_sort_single_element(self):
        """Тестирование сортировки списка с одним элементом (граничное значение)."""
        assert bubble_sort([42]) == [42]

    def test_bubble_sort_with_duplicates(self):
        """Тестирование сортировки списка с дубликатами."""
        assert bubble_sort([5, 2, 8, 2, 5]) == [2, 2, 5, 5, 8]

    def test_bubble_sort_with_floats(self):
        """Тестирование сортировки списка с дробными числами."""
        assert bubble_sort([3.5, 1.2, 4.8, 2.1]) == [1.2, 2.1, 3.5, 4.8]

    # Негатив
    def test_bubble_sort_invalid_input_type(self):
        """Тестирование реакции на неверный тип входных данных (не список)."""
        with pytest.raises(TypeError):
            bubble_sort("не список")
        with pytest.raises(TypeError):
            bubble_sort(123)

    def test_bubble_sort_invalid_element_type(self):
        """Тестирование реакции на список с нечисловыми элементами."""
        with pytest.raises(TypeError):
            bubble_sort([1, 2, 'a', 4])


class TestSieveOfEratosthenes:

    # Позитив
    def test_sieve_small_n(self):
        """Тестирование для малых значений n, включая граничное n=2."""
        assert sieve_of_eratosthenes(2) == [2] # Граничное значение
        assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
        assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_sieve_n_is_prime(self):
        """Тестирование, когда n является простым числом."""
        assert sieve_of_eratosthenes(13) == [2, 3, 5, 7, 11, 13]

    def test_sieve_n_is_not_prime(self):
        """Тестирование, когда n не является простым числом."""
        assert sieve_of_eratosthenes(12) == [2, 3, 5, 7, 11]

    # Негатив
    def test_sieve_negative_n(self):
        """Тестирование реакции на n < 2."""
        # Для n < 2 функция должна вернуть пустой список, а не выбросить исключение
        assert sieve_of_eratosthenes(1) == [] # Граничное значение
        assert sieve_of_eratosthenes(0) == [] # Граничное значение
        assert sieve_of_eratosthenes(-100) == []

    def test_sieve_invalid_type(self):
        """Тестирование реакции на нецелый тип данных."""
        with pytest.raises(TypeError):
            sieve_of_eratosthenes(10.5)