
#1 Створити список із 10-ти чисел посортувати і вивести їх.

list_1 = [1,235,4,5,44,755,38,47,8]
list_1.sort()
print (list_1)

#2 Вивести в консоль елементи списку менші за 100.

list_2 = [1,235,4,5,44,755,38,47,8]
list_2.sort()
for roblox in list_2:
    if roblox < 100:
        print(roblox)

#3 Написати программу яка знайде найбільше число у списку.

list_3 = [1,235,4,5,44,755,38,47,8]
list_3.sort()
minecraft = 0
for python in list_3:
  if python > minecraft:
    print (minecraft)

#4 Зробити программу яка знадй найменший елемент списку.

list_4 = [1,235,4,5,44,755,38,47,8]
list_4.sort()
list_4.reverse()
min_value = 0
for torch in list_4:
 min_value = min_value + torch
print(min_value)

#5 Переписати программу та поставити коміти над функціями та змінними який простір імен в них.

value = 1  #Глобальна

def first():  #Глобальна
    value = 10  #Глобальна
    def second():  #Локальна
        print(value)  #Вбудована
    second()  #Нелокальна


first()  #Нелокальна
print(value)  #Вбудована

#5 Переписати приклад

def first():
    value = 10
    my_value = 1
    global newValue
    newValue = 123
    #Локально
    def second():
        nonlocal my_value
        my_value = 5
        #Вбудована
        print(value)
    second()
    print(my_value)

first()
#Вбудована
print(value)
print(newValue)

#6 Створити гру камінь, ножниці, папір.

import random
def game(user_choice,result):
    print("<========Start Game========>")

    computer_choice = random.choice("rps")

    if user_choice == "r" and computer_choice == "p":
        result["computer"] += 1
        print("User_choice:", user_choice, "Computer choice: ", computer_choice)
        print("Score: Computer ", result["computer"],"-",result['user'],"User")
    elif user_choice == "p" and computer_choice == "s":
        result["computer"] += 1
        print("User_choice:", user_choice, "Computer choice: ", computer_choice)
        print("Score: Computer ", result["computer"], "-", result['user'], "User")
    elif user_choice == "s" and computer_choice == "r":
        result["computer"] += 1
        print("User_choice:", user_choice, "Computer choice: ", computer_choice)
        print("Score: Computer ", result["computer"], "-", result['user'], "User")

    if user_choice == "p" and computer_choice == "r":
        result["user"] += 1
        print("User_choice:", user_choice, "Computer choice: ", computer_choice)
        print("Score: Computer ", result["computer"], "-", result['user'], "User")
    elif user_choice == "s" and computer_choice == "p":
        result["user"] += 1
        print("User_choice:", user_choice, "Computer choice: ", computer_choice)
        print("Score: Computer ", result["computer"], "-", result['user'], "User")
    elif user_choice == "r" and computer_choice == "s":
        result["user"] += 1
        print("User_choice:", user_choice, "Computer choice: ", computer_choice)
        print("Score: Computer ", result["computer"], "-", result['user'], "User")
    else :
        result["user"]+=1
        result["computer"]+=1
        print("EQUAL")

result = {"computer": 0, "user":0}
choice = input("Enter r p s: ===> ")



