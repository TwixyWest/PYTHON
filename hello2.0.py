# my_list = list()
#
#
# for i in range(5):
#     anw = input()
#     my_list.append(anw)
#
# myTuple = tuple(my_list)
# print(type(myTuple))
# print(myTuple)

# userTypes = ('admin', 'student', 'teacher', 'moderator', 'member')
# userTypes2 = ('user', 'newbee', 'customer')
# tuple3 = userTypes + userTypes2
# print(type(tuple3))
# print(tuple3.index('user'))
# for u in userTypes:
#     print(u)
#
# for index in range(len(userTypes)):
#     print(userTypes[index])
#ЗАВДАННЯ 1

fruits = ("яблуко", "банан", "апельсин", "Blox Fruits", "яблуко", "груша", "яблуко", "апельсин", "Blox Fruits", "One piece")
user_input = input("Введіть назву фрукта: ")
count = fruits.count(user_input)
print(f"Кількість фруктів '{user_input}' у кортежі: {count}")

#ЗАВДАННЯ 2

fruits = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
user_input = input("Введіть назву фрукта: ")
count_exact = fruits.count(user_input)
count_partial = sum(1 for fruit in fruits if user_input in fruit)
print(f"Кількість точних збігів '{user_input}' у кортежі: {count_exact}")
print(f"Кількість часткових збігів '{user_input}' у кортежі: {count_partial}")

#ЗАВДАННЯ 3

Thewither3 = ("Toyota", "Ford", "BMW", "Toyota", "Honda", "Toyota", "москвич", "москвич")
old_name = input("Введіть назву виробника для заміни: ")
new_name = input("Введіть нове слово для заміни: ")
Thewither3_list = list(Thewither3)
Thewither3_list = [new_name if manufacturer == old_name else manufacturer for manufacturer in Thewither3_list]
Thewither3 = tuple(Thewither3_list)
print("Оновлений кортеж:", Thewither3)

#Завдання 4

numbers = (1, 23, 456, 78, 9, 1234, 567, 89, 12, 3456, 3453, 453)
digit_count = {}

for number in numbers:
    count = len(str(abs(number)))
    if count in digit_count:
        digit_count[count] += 1
    else:
        digit_count[count] = 1

for digits, elements in sorted(digit_count.items()):
    print(f"{digits} цифра(и) — {elements} елемент(и)")

