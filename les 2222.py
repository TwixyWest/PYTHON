# # Завдання 1
# try:
#     a = float(input("Введіть перше число для ділення: "))
#     b = float(input("Введіть друге число для ділення: "))
#     print("Результат ділення:", a / b)
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль, сергусь виправи пж")
#
# # Завдання 2
# def divide_numbers(num1, num2):
#     return num1 / num2
#
# try:
#     print("Результат функції (обробка зовні):", divide_numbers(a, b))
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль, сергусь виправи пж")
#
# def numbers_internal(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return "Помилка: ділення на нуль, сергусь виправи пж"
#
# print("Результат функції (обробка всередині):", numbers_internal(a, b))
#
# # Завдання 3
# try:
#     s = input("Введіть рядок для перетворення в число: ")
#     print("Результат перетворення:", float(s))
# except ValueError:
#     print("Помилка: неможливо перетворити рядок на число.")
#
# # Завдання 4
# def string_to_number_external(string):
#     return float(string)
#
# try:
#     print("Результат функції :", string_to_number_external(s))
# except ValueError:
#     print("Помилка: неможливо перетворити рядок на число.")
#
# # Завдання 4
# def string_to_number_internal(string):
#     try:
#         return float(string)
#     except ValueError:
#         return "Помилка: неможливо перетворити рядок на число."
#
# print("Результат функції :", string_to_number_internal(s))


import math

# Завдання 1
try:
    num = float(input("Введіть число для обчислення квадратного кореня: "))
    if num < 0:
        raise ValueError("Від'ємне число. Неможливо обчислити квадратний корінь.")
    print("Квадратний корінь числа:", math.sqrt(num))
except ValueError as e:
    print("Помилка:", e)

# Завдання 2
def square_root(num):
    try:
        if num < 0:
            raise ValueError("Від'ємне число. Неможливо обчислити квадратний корінь.")
        return math.sqrt(num)
    except ValueError as e:
        return f"Помилка: {e}"

num = float(input("Введіть число для функції: "))
print("Результат функції:", square_root(num))

# Завдання 3 і 4
dictionary = {}

def add_to_dictionary(key, value):
    dictionary[key] = value

def display_dictionary():
    return dictionary

def find_value(key):
    return dictionary.get(key, "Помилка: ключ не знайдено.")

def update_value(key, value):
    if key in dictionary:
        dictionary[key] = value
        return "Значення оновлено."
    return "Помилка: ключ не знайдено."

def delete_key(key):
    if key in dictionary:
        del dictionary[key]
        return "Пара видалена."
    return "Помилка: ключ не знайдено."
