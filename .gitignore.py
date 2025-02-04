# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     def init(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     @abstractmethod
#     def show_trans(self):
#         pass
#
#     @abstractmethod
#     def show_speed(self):
#         pass
#
# class CAR(Transport):
#     def init(self, name, speed):
#         super().init(name, speed)
#
#     def show_trans(self):
#         return f"Name: {self.name}, speed: {self.speed}"
#
#     def show_speed(self):
#         return f"Speed: {self.speed} "
#
# class Moto(Transport):
#     def init(self, name, speed, type):
#         super().init(name, speed)
#         self.type = type
#
#     def show_trans(self):
#         return f"Name: {self.name}, speed: {self.speed}  type: {self.type}"
#
#     def show_speed(self):
#         return f"Швидкість: {self.speed} км"
# car_obj = CAR("фвафаівв", 11230)
# moto_obj = Moto("вфііфвi", 151233, "фівфів")

# print(car_obj.show_trans())
# print(car_obj.show_speed())
#
# print(moto_obj.show_trans())
# print(moto_obj.show_speed())


# from abc import abstractmethod
# class Transport:
#     @abstractmethod
#     def show_transport(self):
#         pass
#
#     @abstractmethod
#     def set_speed(self):
#         pass
#
#
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
import os
#
# file = open("text.txt", "w")
# file.write("IT STEP")
# file.close()
# file = open("IT STEPTest.txt","w")
# inf = ""
# while inf !="stop":
#     inf = input("information:").lower()
#     file.write(inf)
#
# file.close()
#
# with open("Newdile.txt", "w") as itstepFile:
#     itstepFile.write("NEW INFO")
#
# with open(file, "r") as myFile:
#     print(myFile.readlines())
file = "I.txt"
name = int(input("n: "))
age = int(input("n: "))
birth = int(input("n: "))
id = int(input("n:"))
with open ("Newww.thx", "w") as IFile:
    IFile.write(f"name: {name}")
    IFile.write(f"age: {age}")
    IFile.write(f"birth: {birth}")
    IFile.write(f"id: {id}")




with open (file,"r") as myFile:
    print(myFile.readlines())




