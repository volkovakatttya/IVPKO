"""
Библиотека математических функций для лабораторной работы по тестированию.
"""

def fibonacci(n):
    """
    Возвращает список из n первых чисел Фибоначчи.

    Args:
        n (int): Количество чисел Фибоначчи для генерации.

    Returns:
        list: Список чисел Фибоначчи.

    Raises:
        TypeError: Если n не целое число.
        ValueError: Если n отрицательное.
    """
    # Проверка на корректный тип входных данных
    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом")
    # Проверка на граничное значение (нижняя граница)
    if n < 0:
        raise ValueError("n не может быть отрицательным")

    # Обработка базовых случаев
    if n == 0:
        return []
    elif n == 1:
        return [0]

    # Генерация последовательности для n >= 2
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)
    return fib_sequence


def bubble_sort(numbers):
    """
    Сортирует список чисел методом пузырьковой сортировки.

    Args:
        numbers (list): Список чисел для сортировки.

    Returns:
        list: Отсортированная по возрастанию копия списка.

    Raises:
        TypeError: Если входные данные не являются списком или
                   если элементы списка не числа (int или float).
    """
    # Проверка на корректный тип входных данных
    if not isinstance(numbers, list):
        raise TypeError("Входными данными должен быть список")

    # Создаем копию списка, чтобы не изменять оригинал
    sorted_list = numbers.copy()
    n = len(sorted_list)

    # Проверка типов элементов списка
    for item in sorted_list:
        if not isinstance(item, (int, float)):
            raise TypeError("Все элементы в списке должны быть числами")

    # Алгоритм пузырьковой сортировки
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
        # Если внутренний цикл не произвел обменов, список отсортирован
        if not swapped:
            break
    return sorted_list


def sieve_of_eratosthenes(n):
    """
    Возвращает список всех простых чисел до n (включительно, если n простое)
    с помощью алгоритма Решето Эратосфена.

    Args:
        n (int): Верхняя граница для поиска простых чисел.

    Returns:
        list: Список простых чисел <= n.

    Raises:
        TypeError: Если n не целое число.
        ValueError: Если n меньше 2.
    """
    # Проверка на корректный тип входных данных
    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом")
    # Проверка на граничное значение (нижняя граница для алгоритма)
    if n < 2:
        return []  # Нет простых чисел меньше 2

    # Инициализация списка: is_prime[i] = True, если i простое
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми их отсеяли

    # Алгоритм Решето Эратосфена
    for i in range(2, int(n**0.5) + 1): # корень чтоб ниже не выпасть за пределы n при i*i
        if is_prime[i]:
            # Помечаем все кратные i числа как не простые
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # Формируем список простых чисел
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes