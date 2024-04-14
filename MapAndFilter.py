numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Функция для возведения в квадрат
def oper(num):
    new_num = num ** 2
    print(new_num)

# Функция для возведения в квадрат и отбора нечетных значений
def odd(num):
    new_num = num ** 2
    if new_num % 2 != 0:
        print(new_num)


print('Элементы списка возведены в квадрат')
list(map(oper, numbers))
print('Элементы списка возведены в квадрат и выбраны нечетные числа')
list(filter(odd, numbers))
