class Person:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def show(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Id: {self.id}")


class Student(Person):
    def __init__(self, name, surname, id):
        super().__init__(name, surname, id)


class Worker(Student):
    def __init__(self, name, surname, id, age, hours_of_work, salary):
        super().__init__(name, surname, id)
        self.age = age
        self.hours_of_work = hours_of_work
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: {self.salary}")
class Teacher(Worker):
    def __init__(self, name, surname, id, age, hours_of_work, salary, count_of_group, size_of_group):
        super().__init__(name, surname, id, age, hours_of_work, salary)
        self.count_of_group = count_of_group
        self.size_of_group = size_of_group
        self.group = []

    def add_student(self, student):
        if len(self.group) < self.size_of_group:
            self.group.append(student)
            print(f"Student {student.name} added to the group.")
        else:
            print("The group is full!")


teacher = Teacher("asdsad", "asdasd", "1", 35, 40, 3000, 1, 3)
student1 = Student("sdasad", "saddsa", "2")
student2 = Student("hsdd", "dasdsa", "3")

teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(Student("dasasd", "dsasad", "4"))
teacher.add_student(Student("asdasd", "asdasd", "5"))
teacher.update_salary(3500)

teacher.show()

#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def show(self):
#         print(f"Title: {self.title} Author: {self.author} count of pages: {self.pages}")
#
# class Magazine(Book):
#     def __init__(self, title, author, pages, sponsored, pictures):
#         super().__init__(title, author, pages)
#         self.sponsored = sponsored
#         self.pictures = pictures
#
#     def show(self):
#         print(f"Title: {self.title} Author: {self.author} count of pages: {self.pages} sponsored {self.sponsored}, pictures {self.pictures}")
#
#
# class EBook(Book):
#     def __init__(self, title, author, pages, can_be_downloaded, price):
#         super().__init__(title, author, pages)
#         self.can_be_downloaded = can_be_downloaded
#         self.price = price
#     def show(self):
#         print(f"Title: {self.title} Author: {self.author} count of pages: {self.pages} can be downloaded: {self.can_be_downloaded}, price: {self.price} ")
#
# class EMagazin(Book):
#     def __init__(self, title, author, pages, can_be_downloaded, price, count):
#         super().__init__(title, author, pages)
#         self.can_be_downloaded = can_be_downloaded
#         self.price = price
#         self.count = count
#     def show(self):
#         print(f"Title: {self.title} Author: {self.author} count of pages: {self.pages} can be downloaded: {self.can_be_downloaded}, price: {self.price}, count {self.count} ")
#
# obj = Book("my day", "Puschkin", 125)
# obj.show()
# obj1 = Magazine("ghdfd", "asdasd", 26, "sfd", 10)
# obj1.show()
# obj2 = EMagazin("sdfsdf", "dasasd", 35, True, 1, 6)
# obj2.show()
# obj3 = EBook("mikoa", "odsa", 10, False, 10)
# obj3.show()

# class A:
#     def show(self):
#         print("class A")
#
# class B(A):
#     def show1(self):
#         print("class B")
#
# class C(B):
#     def show2(self):
#         print("class C")
#
# class E(C):
#     def show3(self):
#         print("class E")
#
# obj = E()
#
# print(E.mro())
# print(isinstance(obj, C))
# print(issubclass(E, A))