from math import isqrt

# Функция для проверки является ли число простым
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

# Декоратор для проверки на простое число
def is_prime_decorator(func):
    def wrapper(*args):
        result = func(*args)
        if is_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

# Функция для сложения трех чисел
@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)