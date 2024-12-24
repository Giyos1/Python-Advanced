# # class Student:
# #     def __init__(self, name, age, grades):
# #         self.name = name
# #         self.age = age
# #         self.grades = grades
# #
# #     def get_info(self):  # self = student2
# #         print(f"Talabaning ismi {self.name}, yoshi {self.age}, bahosi {self.grades}")
# #
# #
# # a = 12
# # student1 = Student("Giyos", 25, "5")
# # student2 = Student("Aziz", 28, "5")
# # print(student1.age)
# # print(student1.name)
# # print(student1.grades)
# # student1.get_info()
# # print(student2.age)
# # print(student2.name)
# # print(student2.get_info())
# #
# # a = "salom"
# # print(a.upper())
#
# # class User:
# #     def __init__(self, name, username, email):
# #         self.name = name
# #         self.username = username
# #         self.email = email
# #
# #     def get_info(self):
# #         print(f"{self.name},{self.username},{self.email}")
# #         # return f"{self.name},{self.username},{self.email}"
# #
# #
# # user1 = User("Ali0", "Vali", "email@gmail.com")
# # user1.get_info()
# # print(user1.email)
# class Book:
#     def __init__(self, ISBN, name, subject, dds_number, authors=[]):
#         self.ISBN = ISBN
#         self.name = name
#         self.subject = subject
#         self.dds_number = dds_number
#         self.authors = authors
#
#     def get_info(self):
#         return f'{self.name, self.subject}'
#
#     def get_name(self):
#         return self.name
#
#     def get_subject(self):
#         return self.subject
#
#
# class Catalog:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def search(self, name="", author=""):
#         if name:
#             book = []
#             for i in self.books:
#                 if i.name == name:
#                     book.append(i)
#             if book:
#                 for i in book:
#                     print(f"bu kitob {i.dds_number} da")
#             else:
#                 print("topilmadi")
#
#     def add_book(self, book: Book):
#         if isinstance(book, Book):
#             self.books.append(book)
#             print(f"sizning {book.get_info()} qoshildi ")
#         else:
#             print("siz Book classiga tegishli malumot bering")
#
#
# class Author:
#     def __init__(self, name):
#         self.name = name
#
#     def get_info(self):
#         return f"{self.name}"
#
#
# catolg1 = Catalog("1-javon")
#
# author1 = Author("Azim To'rayev")
# author2 = Author("Mirqosim Jo'rayev")
# author3 = Author("Gafur G'ulom")
#
# book1 = Book("121221", "ona tili 5", "darslik", "1231", [author1, author2])
# book2 = Book("121123221", "rus tili 5", "darslik", "3231", [author3, author2])
# book3 = Book("125653221", "engliz tili 5", "darslik", "9231", [author3, author2])
#
# catolg1.add_book(book1)
# catolg1.add_book(book2)
# catolg1.add_book(book3)
# catolg1.search("ona tili 5")
#
# print(book2.name)
# print(book2.get_name())
#
# # print(dir(int))
#
# # for i in dir(Book):
# #     if not i.startswith("__"):
# #         print(i)

# from oop import User
#
# u1 = User("asa", 12)
# print(u1._password)
#
# from oop_16 import Avto, Talaba
#
# a = Avto()
# print(Avto.get_avto_number())

from abc import ABC, abstractmethod


class Author:
    def __init__(self, name):
        self.name = name


class LibraryItem(ABC):
    __item = 0

    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject
        LibraryItem.__item += 1

    @classmethod
    def get_items(cls):
        return cls.__item

    @abstractmethod
    def locate(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, upc, subject, isbn, dds_number):
        super().__init__(title, upc, subject)
        self.__isbn = isbn  # incapsulation
        self.dds_number = dds_number
        self.authors = []

    def set_authors(self, author: Author):
        pass

    def locate(self):
        return self.dds_number

    def get_info(self):
        return f"{self.title}"


class DVD(LibraryItem):
    def __init__(self, title, janr):
        super().__init__(title, upc=None, subject=None)
        self.janr = janr

    def locate(self):
        return self.janr + " " + self.title

    def get_info(self):
        return f"{self.title}"


class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: Book | DVD):
        self.items.append(item)

    def search(self, keyword):
        item = []
        # if keyword in self.items:
        for i in self.items:
            if i.title == keyword:
                item.append(i.locate())
        return item


book1 = Book("asas", "asasas", "asas", "1231323", "1234")
dvd = DVD("asas", "asass")
# print(book1.locate())
catalog = Catalog()
catalog.add_item(book1)
catalog.add_item(dvd)

print([i for i in catalog.search("asas")])


class A:
    __a = 0

    @classmethod
    @property
    def a(cls):
        return cls.__a

    @classmethod
    @a.setter
    def a(cls, a):
        cls.__a = a


a = A()
print(A.a)
A.a = 1
# print(A.a)
