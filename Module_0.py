# Задача 1: Мы используем оператор возведения в степень ** и умножение, чтобы получить результат 15.0.
print(9 ** 0.5 * 5)

# Задача 2: Мы используем логические операторы and для проверки двух условий одновременно.
print(9.99 > 9.98 and 1000 != 1000.1)

# Задача 3: Мы демонстрируем разницу между выражениями с приоритетом и без него, а затем сравниваем их результаты.
print(2 * 2 + 2)  # без приоритета
print(2 * (2 + 2))  # с приоритетом для сложения
print((2 * 2 + 2) == (2 * (2 + 2)))  # сравнение

# Задача 4: Мы преобразуем строку в число, смещаем десятичную точку, а затем используем целочисленное деление
# и остаток от деления, чтобы получить первую цифру после запятой.
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Смещаем 4 в целую часть
first_digit_after_dot = int(shifted_number) % 10  # Получаем первую цифру после запятой
print(first_digit_after_dot)