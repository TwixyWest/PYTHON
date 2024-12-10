# list = [8, 9, 14, 11]
# list.append(6) #елемент в кінец списку
# list.insert(1, 10) #додає еленент на певну позицію
# list.remove(9) #удаляє 1 щось
# print(list.index(8)) #повертає позиціюю і разує від 1
# print(list[0]) #витягує шота
# # list.clear()
# print(list)

# list = []
# number = int(input("Insert counts of Elements: "))
# for i in range(number):
#     element = input("Element: ")
#     list.append(element)
#
# print(list)

# list = []
# n = int(input('Скільки елементів ви хочете додати до списку?: '))
# for i in range(n):
#     element = int(input(f"Введіть елемент {i +1}: "))
#     list.append(element)
# positive_elements = [x for x in list if x > 0]
# print("Позитивні елементи списку", positive_elements)

# list = [9, 4, 5, 6]
# list.sort()
# print(list)
#
# list.reverse()
# print(list)

# list = []
# words = input("Введіть слова: ").split()
# palindrom = [word for word in words if word == word[::-1]]
#
# print("Слова-паліндроми:", palindrom)

# list = []
# words = input("Введіть слова: ").split()
# palindrom = []
# for word in words:
#     if word == word[::-1]:
#         palindrom.append(word)
# print("Слова-паліндроми:", palindrom)
# l = []
# l= list()

# word = "abc"
# chars = list(word)
# chars.reverse()
# print(chars)

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.publication_year = year
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Genre: {self.genre}")

books = []

for i in range(3):
    title = input(f"Enter title for book {i + 1}: ")
    author = input(f"Enter author for book {i + 1}: ")
    year = input(f"Enter publication year for book {i + 1}: ")
    genre = input(f"Enter genre for book {i + 1}: ")
    book = Book(title, author, year, genre)
    books.append(book)

    books.sort(key=lambda michaillox:michaillox.publication_year)

def get_book_by_author(books, author):
    result = []
    for book in books:
        if(book.author.lower() == author.lower()):
            result.append(book)
            return result
for book in books:
    book.display_info()

    print()