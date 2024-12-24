# list1 = [1, 2, 3, 4, 5, 6, 7]
#
# list_itator = iter(list1)
# print(list_itator)
# print(next(list_itator))
# print(next(list_itator))
# print(next(list_itator))
# print(next(list_itator))
# print(next(list_itator))
# print(next(list_itator))
# print(next(list_itator))
# print(next(list_itator))
#
# for i in list1:
#     print(i)

# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         # print("1")
#         return self
#
#     def __next__(self):
#         print("next")
#         if self.current >= self.end:
#             raise StopIteration("xatolik")
#         self.current += 1  # 1
#         return self.current - 1
#
#
# m = MyIterator(0, 12)

# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# for i in m:
#     print(i)

# class CheksizIterator:
#     def __init__(self):
#         self.num = 1
#
#     def __iter__(self):
#         # print("1")
#         return self
#
#     def __next__(self):
#         self.num += 2
#         return self.num - 2
#
#
# a = CheksizIterator()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)
#
# class Unversitet:
#     def __init__(self, name):
#         self.name = name
#         self.talabalar = []
#
#     def add_student(self, student):
#         if isinstance(student, Talabalar):
#             self.talabalar.append(student)
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index == len(self.talabalar):
#             raise StopIteration
#         self.index += 1
#         return self.talabalar[self.index - 1].name
#
#
# class Talabalar:
#     def __init__(self, name, bosqich):
#         self.name = name
#         self.bosqich = bosqich
#
#
# student1 = Talabalar("ali", 2)
# student2 = Talabalar("vali", 2)
# student3 = Talabalar("gani", 2)
# student4 = Talabalar("maqsud", 2)
#
# unversitet = Unversitet("TATU")
# unversitet.add_student(student1)
# unversitet.add_student(student2)
# unversitet.add_student(student3)
# unversitet.add_student(student4)
#
# for i in unversitet:
#     print(i)
#
# def yrange(n):
#     i = 0
#     print("birinchis")
#     while i < n:
#         print("yield", i + 1)
#         yield i  # 0
#         i += 1  # 1
#         print("yield", i + 1)
#
#
# a = yrange(12)
# print(a)
#
# # for i in a:
# #     print(i)
# 1. fileni oqiymiz(file type xoxishiy)
# 2. shu fildi oqishda xatolik bolsa log filga yozamiz "a" modeda hamda consolga chiqaramiz
# 3. log fileda bor malumotlarni oqiymiz va consolga chiqaramiz
"""
2024-12-17 18:55:14,275 - ERROR - FileNotFoundError mana bu "file" topilmadi
2024-12-17 18:55:14,275 - ERROR - FileNotFoundError mana bu "file" topilmadi
2024-12-17 18:55:14,275 - ERROR - FileNotFoundError mana bu "file" topilmadi
2024-12-17 18:55:14,275 - ERROR - FileNotFoundError mana bu "file" topilmadi
"""
print("")