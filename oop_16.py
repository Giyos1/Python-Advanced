class A:
    def get_info(self):
        return f"A class ishladi"


#
#
# class B:
#     def get_info(self):
#         return f"B class ishladi"


# class C(A, B):
#     def get_info(self):
#         return f"C class ishladi"
#
#
# c1 = C()
# print(c1.get_info())
#
# user_list = ["username", "admin", "hk"]
#
#
# class User:
#     def __init__(self, username, password, first_name, last_name):
#         self.__username = username
#         self.__password = password
#         self.first_name = first_name
#         self.last_name = last_name

# def get_username(self):
#     return self.__username
#
# def set_username(self, username):
#     if username in user_list:
#         return "already exist"
#     self.__username = username
#     return self.__username
#
# def set_password(self,password):
#     pass
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, username):
#         # validation
#
#         self.__username = username
#
#
# u1 = User("admin", "12","as","sasas")
# # print(u1.get_username())
# print(u1.username)
# u1.username = "ali"
# print(u1.full_name)
# print(u1.username)
#
# from abc import ABC, abstractmethod
#
#
# class Tolov(ABC):
#     def __init__(self, card_number, expire_date, summa):
#         self.card_number = card_number
#         self.expire_date = expire_date
#         self.summa = summa
#
#     @abstractmethod
#     def summa_yechivolish(self):
#         pass


# class PayMe(Tolov):
#     def summa_yechivolish(self):
#         print("payme bilan bogkliq summani yechib olish algaritimi ketadi")
#
#
# p = PayMe("4343", "12/25", "121212")
# p.summa_yechivolish()
# class BankATM(ATM):
#     def insert_cart(self):
#         print("kartani ishlatingiz")

#
# a = BankATM()
# print(a.insert_cart())

class Talaba:
    universitet = "TATU"

    def __init__(self):
        pass

    @classmethod
    def update_unversitet(cls, unversitet):
        cls.universitet = unversitet
        print(cls.universitet)
        return cls.universitet


#
# Talaba.universitet = "INHA"
# print(Talaba.universitet)
# Talaba.update_unversitet("INHA")

class Avto:
    __avto_number = 0

    def __init__(self):
        Avto.__avto_number += 1

    @classmethod
    def get_avto_number(cls):
        return cls.__avto_number


# a1 = Avto()
# print(Avto.get_avto_number())
# a2 = Avto()
# print(Avto.get_avto_number())