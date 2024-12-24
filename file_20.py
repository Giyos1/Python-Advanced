# fayl = open("data.txt")
# data = fayl.read()
# print(data)
# fayl.close()

# with open("data.txt") as fayl:
#     list1 = []
#     for i in fayl:
#         list1.append(i)
# print(list1)
# try:
#     with open("data1.txt") as fayl:
#         data = fayl.readlines()
# except FileNotFoundError as e:
#     print(e)
# list1 = []
# for i in data:
#     list1.append(i.rstrip())
# print(list1)

# with open("data.txt", "w") as fayl:
#     fayl.write("1234\n")
#     fayl.write("salom")

# with open("data.txt", "a") as fayl:
#     fayl.write("1234\n")
#     fayl.write("salom\n")

with open("data1.txt", "r+") as fayl:
    fayl.write("1234\n")
    fayl.write("salom\n")
#
#     fayl.seek(0)
#     data = fayl.readlines()
# print(data)
#
# with open("data1.txt", "a+") as fayl:
#     fayl.write("1234\n")
#     fayl.write("salom\n")
#
#     fayl.seek(0)
#     data = fayl.readlines()
# print(data)

import pickle

# class Talaba:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} talaba, yoshi:{self.age}"
#
#
# talaba1 = Talaba("firdavs", "12")
# talaba2 = Talaba("firdavs2", "12")
#
# with open("info.dat", "ab+") as fayl:
#     pickle.dump(talaba1, fayl)
#     pickle.dump(talaba2, fayl)
#
#     fayl.seek(0)
#     while True:
#         try:
#             obj = pickle.load(fayl)
#             print(obj)
#         except EOFError:
#             break
# # with open("info.dat", "ab+") as fayl:
# #     pickle.dump(talaba2, fayl)

from abc import ABC, abstractmethod


class LibrarySystem(ABC):
    __total_items = 0

    def __init__(self, Title, UPC, Subject):
        self.Title = Title
        self.UPC = UPC
        self.Subject = Subject
        LibrarySystem.__total_items += 1

    @abstractmethod
    def locate(self) -> str:
        return self.UPC

    @classmethod
    def get_total_number_of_items(cls):
        return cls.__total_items


class Author:
    def __init__(self, author_name):
        self.author_name = author_name

    def get_author_name(self) -> str:
        return self.author_name

    def set_author_name(self, name: str) -> None:
        self.author_name = name


class Book(LibrarySystem):
    __total_books = 0

    def __init__(self, ISBN, Authors: list[Author], Title, Subject, DDS_number, UPC):
        super().__init__(Title=Title, UPC=UPC, Subject=Subject)
        self.ISBN = ISBN
        self.Authors = Authors
        self.DDS_number = DDS_number
        Book.__total_books += 1

    def get_info(self) -> str:
        authors = [author.author_name for author in self.Authors]
        res = ", ".join(authors)
        return f"\n\t\tKitob ma\'lumotlari:\nKitob nomi: {self.Title} \nKitob ISBN: {self.ISBN} \nKitob mualliflari: {res} \nKitob DDS raqami: {self.DDS_number}, \nKitob UPC raqami: {self.UPC}, \nKitob janri: {self.Subject}"

    def set_book_title(self, title: str) -> None:
        self.Title = title

    def set_book_subject(self, subject: str) -> None:
        self.Subject = subject

    def set_book_ISBN(self, ISBN: str) -> None:
        self.ISBN = ISBN

    def set_book_upc(self, UPC: str) -> None:
        self.UPC = UPC

    def set_book_DSS_number(self, DDS_number: str) -> None:
        self.DDS_number = DDS_number

    def set_book_authors(self, authors: list[Author]) -> None:
        self.Authors = authors

    def locate(self) -> str:
        return f"UPC number: {self.UPC}, ISBN number: {self.ISBN}"

    @classmethod
    def get_total_number_of_books(cls):
        return cls.__total_books


class Magazine(LibrarySystem):
    __total_magazines = 0

    def __init__(self, Volume: int, Issue: int):
        super().__init__(Title=None, UPC=None, Subject=None)
        self.Volume = Volume
        self.Issue = Issue

    def get_magazine_info(self) -> str:
        if not self.Issue and not self.Volume:
            return "Hech qanday jurnal ma\'lumotlari yo\'q!"
        else:
            return f"Jurnal hajmi: {self.Volume}, Jurnal chop etilgan yili: {self.Issue}"

    def locate(self) -> str:
        return f"UPC number: {self.UPC}"

    @classmethod
    def get_total_number_of_magazines(cls):
        return cls.__total_magazines


class DVD(LibrarySystem):
    __total_DVDs = 0

    def __init__(self, Title, UPC, Actors: list[str], Director, Genre):
        super().__init__(Title=Title, UPC=UPC, Subject=None)
        self.Actors = Actors
        self.Director = Director
        self.Genre = Genre

    def get_dvd_info(self) -> str:
        if not self.Actors and not self.Director and not self.Genre:
            return "Hech qanday DVD disk ma\'lumotlari yo\'q!"
        else:
            text = [actor for actor in self.Actors]
            res = ", ".join(text)
            return f"DVD aktyorlari: {res}, DVD Direktori: {self.Director}, DVD Janri: {self.Genre}"

    def locate(self) -> str:
        return f"UPC number: {self.UPC}"

    @classmethod
    def get_total_number_of_DVDs(cls):
        return cls.__total_DVDs


class CD(LibrarySystem):
    __total_CDs = 0

    def __init__(self, Artist: list[str]):
        super().__init__(Title=None, UPC=None, Subject=None)
        self.Artist = Artist

    def get_cd_info(self) -> str:
        if not self.Artist:
            return "Hech qanday CD disk ma\'lumotlari yo\'q!"
        else:
            text = [artist for artist in self.Artist]
            res = ", ".join(text)
            return f"CD artistlari: {res}"

    def locate(self) -> str:
        return f"UPC number: {self.UPC}"

    @classmethod
    def get_total_number_of_CDs(cls):
        return cls.__total_CDs


class Catalog:
    def __init__(self):
        self.books = []
        self.cd_disks = []
        self.dvd_disks = []
        self.magazines = []

    def search_book(self, name="", author=""):
        try:
            if not name and not author:
                raise ValueError("Izlash uchun kiritilgan ma'lumotlar yo'q!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return
        for book in self.books:
            author_names = [a.author_name for a in book.Authors]
            if (name and book.Title == name) or (author and author in author_names):
                print(f"Kitob topildi: {book.Title}, DDS raqami: {book.DDS_number}, UPC: {book.UPC}")
                return
        print("Bunday kitob katalogda yo'q!")

    def search_dvd(self, actor_name="", director="", genre=""):
        try:
            if not actor_name and not director and not genre:
                raise ValueError("DVD izlash uchun bittayam kriteriya berilmagan!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return

        found = False
        for i, dvd in enumerate(self.dvd_disks, 1):
            if (actor_name and actor_name in dvd.Actors) or (director and director == dvd.Director) or (
                    genre and genre == dvd.Genre):
                print(f"DVD topildi. {i}. DVD nomi: {dvd.Title}, UPC raqami: {dvd.UPC}")
                found = True
        if not found:
            print(f"Bunday DVD topilmadi")

    def search_cd(self, artist_name=""):
        try:
            if not artist_name:
                raise ValueError("CD izlash uchun artist nomi kiritilmagan!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return

        found = False
        for i, cd in enumerate(self.cd_disks, 1):
            if artist_name in cd.Artist:
                print(f"CD topildi. {i}. Artist(lar): {', '.join(cd.Artist)}")
                found = True
        if not found:
            print(f"Bunday artistli CD topilmadi.")

    def search_magazine(self, volume=None, issue=None):
        try:
            if volume is None and issue is None:
                raise ValueError("Jurnal izlash uchun hajm yoki chop etilgan yil berilmadi!")
        except ValueError as e:
            print(f"Xatolik! {e}")
            return

        found = False
        for i, magazine in enumerate(self.magazines, 1):
            if (volume is not None and magazine.Volume == volume) or (issue is not None and magazine.Issue == issue):
                print(f"Jurnal topildi. {i}. Hajmi: {magazine.Volume}, Chop etilgan yili: {magazine.Issue}")
                found = True
        if not found:
            print(f"Bunday jurnal topilmadi.")

    def add_book(self, book: Book) -> None:
        try:
            if not book or not isinstance(book, Book):
                raise TypeError("Kitob 'Book' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.books.append(book)
        print(f"{book.Title} nomli kitob katalogga qo'shildi.")

    def add_cd(self, cd: CD) -> None:
        try:
            if not cd or not isinstance(cd, CD):
                raise TypeError("CD 'CD' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.cd_disks.append(cd)
        print(f"{cd.Artist} nomli CD katalogga qo'shildi.")

    def add_dvd(self, dvd: DVD) -> None:
        try:
            if not dvd or not isinstance(dvd, DVD):
                raise TypeError("DVD 'DVD' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.dvd_disks.append(dvd)
        print(f"{dvd.Director} nomli DVD katalogga qo'shildi.")

    def add_magazine(self, magazine: Magazine) -> None:
        try:
            if not magazine or not isinstance(magazine, Magazine):
                raise TypeError("Jurnal 'Magazine' turida bo'lishi kerak!")
        except TypeError as e:
            print(f"Xatolik! {e}")
            return

        self.magazines.append(magazine)
        print(f"Jurnal katalogga qo'shildi. Volume: {magazine.Volume}, Issue: {magazine.Issue}")

    def get_catalog_info(self) -> str:
        text = f"\t\tKatalog ma\'lumotlari:\n"
        if not self.books:
            text += f"Kitoblar: Kitoblar javoni bo\'m bo\'sh!\n"
        else:
            kitob = ""
            books = [book for book in self.books]
            for i, book in enumerate(books, 1):
                authors = [author.author_name for author in book.Authors]
                res = ", ".join(authors)
                kitob += f"{i}. Kitob nomi: {book.Title} \n  Kitob ISBN: {book.ISBN} \n  Kitob mualliflari: {res} \n  Kitob DDS raqami: {book.DDS_number}, \n  Kitob UPC raqami: {book.UPC}, \n  Kitob janri: {book.Subject}\n"
            text += f"{kitob}"
        text += f"Jami kitoblar soni: {Book.get_total_number_of_books()}\n"
        text += "\t\tCD disk ma'lumotlari:\n"
        if not self.cd_disks:
            text += "CD disklar: CD disklar javoni bo'sh!\n"
        else:
            for i, disk in enumerate(self.cd_disks, 1):
                text += f"{i}. CD artistlari: {', '.join(disk.Artist)}\n"
        text += f"Jami CD disklar soni: {CD.get_total_number_of_CDs()}\n"
        text += "\t\tDVD disk ma'lumotlari:\n"
        if not self.dvd_disks:
            text += "DVD disklar: DVD disklar javoni bo'sh!\n"
        else:
            for i, dvd in enumerate(self.dvd_disks, 1):
                actors = ", ".join(dvd.Actors)
                text += (
                    f"{i}. DVD nomi: {dvd.Title} \n Aktyorlar: {actors} \n Rejissor: {dvd.Director} \n Janr: {dvd.Genre}\n")
        text += f"Jami DVD disklar soni: {DVD.get_total_number_of_DVDs()}\n"
        text += "\t\tJurnal ma'lumotlari:\n"
        if not self.magazines:
            text += "Jurnallar: Jurnallar javoni bo'sh!\n"
        else:
            for i, mag in enumerate(self.magazines, 1):
                text += (f"{i}. Jurnal nomi: {mag.Title} \n Hajmi: {mag.Volume} \n Noshir yili: {mag.Issue}\n")
        text += f"Jami jurnallar soni: {Magazine.get_total_number_of_magazines()}\n"
        text += f"\nKatalogda barcha buyumlar soni: {LibrarySystem.get_total_number_of_items()}"

        return text

    def delete_book(self, upc: str) -> None:
        for book in self.books:
            if book.UPC == upc:
                self.books.remove(book)
                print(f"Kitob '{book.Title}' katalogdan o'chirildi.")
                return
        print("Bunday kitob katalogda topilmadi!")

    def delete_cd(self, artist_name: str) -> None:
        for cd in self.cd_disks:
            if artist_name in cd.Artist:
                self.cd_disks.remove(cd)
                print(f"Artist '{artist_name}' nomli CD katalogdan o'chirildi.")
                return
        print("Bunday artistli CD topilmadi!")

    def delete_dvd(self, upc: str) -> None:
        for dvd in self.dvd_disks:
            if dvd.UPC == upc:
                self.dvd_disks.remove(dvd)
                print(f"DVD '{dvd.Title}' katalogdan o'chirildi.")
                return
        print("Bunday DVD katalogda topilmadi!")

    def delete_magazine(self, volume: int, issue: int) -> None:
        for magazine in self.magazines:
            if magazine.Volume == volume and magazine.Issue == issue:
                self.magazines.remove(magazine)
                print(f"Jurnal katalogdan o'chirildi. Hajmi: {volume}, Noshir yili: {issue}")
                return
        print("Bunday jurnal katalogda topilmadi!")


main_menu_choices = ["Yangi buyum qoshish", "Buyumlarni izlash yoki korish", "Katalogdagi barcha buyumlarni korish",
                     "Buyumlarni ochirish", "Chiqish"]
adding_items_choices = ["Yangi kitob qoshish", "Yangi DVD qoshish", "Yangi CD qoshish", "Yangi Jurnal qoshish",
                        "Orqaga"]
deleting_items_choices = ["Kitob o'chirish", "DVD o'chirish", "CD o'chirish", "Jurnal o'chirish", "Orqaga"]
searching_items = ["Kitob izlash", "DVD izlash", "CD izlash", "Jurnal izlash", "Orqaga"]


def display() -> int:
    num_of_choices = 0
    for i, item in enumerate(main_menu_choices, 1):
        num_of_choices += 1
        print(f"{i}. {item}")

    return num_of_choices


def display_adding_items() -> int:
    num_of_choices = 0
    print()
    for i, item in enumerate(adding_items_choices, 1):
        print(f"{i}. {item}")
        num_of_choices += 1
    print()
    return num_of_choices


def display_searching_items() -> None:
    for i, item in enumerate(searching_items, 1):
        print(f"{i}. {item}")


def display_deleting_items() -> int:
    print()
    for i, item in enumerate(deleting_items_choices, 1):
        print(f"{i}. {item}")
    print()
    return len(deleting_items_choices)


def main():
    my_catalog = Catalog()
    while True:
        display()
        while True:
            try:
                user_choice = int(input(f"Qaysi amalni bajarasiz? (1-{len(main_menu_choices)}): "))
                if user_choice < 1 or user_choice > len(main_menu_choices):
                    raise ValueError(f"Tanlov 1 dan {len(main_menu_choices)} gacha bo\'ishi shart!")
                break
            except (TypeError, ValueError) as e:
                print(f"Xatolik! {e}")

        if user_choice == 1:
            display_adding_items()
            while True:
                try:
                    add_choice = int(input(f"Qaysi buyumni qo\'shasiz? (1-{len(adding_items_choices)}): "))
                    if add_choice < 1 or add_choice > len(adding_items_choices):
                        raise ValueError(f"Tanlov 1 dan {len(adding_items_choices)} gacha bo\'ishi shart!")
                    break
                except (TypeError, ValueError) as e:
                    print(f"Xatolik! {e}")

            if add_choice == 1:
                title = input("Kitob nomini kiriting: ")
                subject = input("Kitob subject'ini kiriting: ")
                isbn = input("Kitob ISBN raqamini kiriting: ")
                upc = input("Kitob UPC raqamini kiriting: ")
                dds = input("Kitob DDS raqamini kiriting: ")
                authors_list = input(
                    "Kitob mualliflarini kiriting, bir nechta bo'lsa ,(vergul) bilan ajrating: ").split(",")
                authors = [Author(author.strip()) for author in authors_list]
                book = Book(isbn, authors, title, subject, dds, upc)
                my_catalog.add_book(book)
                print("Kitob muvaffaqiyatli qo'shildi.")

            elif add_choice == 2:
                title = input("DVD nomini kiriting: ")
                upc = input("DVD UPC raqamini kiriting: ")
                actors_list = input(
                    "DVD aktyorlarini kiriting, bir nechta bo'lsa ,(vergul) bilan ajrating: ").split(",")
                director = input("DVD direktorini kiriting: ")
                genre = input("DVD janrini kiriting: ")
                dvd = DVD(title, upc, [actor.strip() for actor in actors_list], director, genre)
                my_catalog.add_dvd(dvd)
                print("DVD muvaffaqiyatli qo'shildi.")

            elif add_choice == 3:
                artist_list = input("CD artistlarini kiriting, bir nechta bo'lsa ,(vergul) bilan ajrating: ").split(
                    ",")
                cd = CD([artist.strip() for artist in artist_list])
                my_catalog.add_cd(cd)
                print("CD muvaffaqiyatli qo'shildi.")

            elif add_choice == 4:
                volume = int(input("Jurnal hajmini kiriting: "))
                issue = int(input("Jurnal nashr yilini kiriting: "))
                magazine = Magazine(volume, issue)
                my_catalog.add_magazine(magazine)
                print("Jurnal muvaffaqiyatli qo'shildi.")

            elif add_choice == 5:
                continue

        elif user_choice == 2:
            display_searching_items()
            while True:
                try:
                    search_choice = int(input(f"Qaysi amalni bajarasiz? (1-{len(searching_items)}): "))
                    if search_choice < 1 or search_choice > len(searching_items):
                        raise ValueError(f"Tanlov 1 dan {len(searching_items)} gacha bo\'ishi shart!")
                    break
                except (TypeError, ValueError) as e:
                    print(f"Xatolik! {e}")

            if search_choice == 1:
                name = input(f"Kitob izlash uchun kitob nomini kiriting, agar bilmasaz enter bosing: ")
                author_name = input(f"Yoki kitobni yozgan avtorlardan birini kiriting, agar bilmasaz enter bosing: ")
                my_catalog.search_book(name, author_name)

            elif search_choice == 2:
                actor = input(f"DVD izlash uchun DVDni aktyorlarini kiriting, agar bilmasaz enter bosing: ")
                director = input(f"Yoki DVDni direktorlarini kiriting, agar bilmasaz enter bosing: ")
                janr = input(f"Yoki DVDni janrini kiriting, agar bilmasaz enter bosing: ")
                my_catalog.search_dvd(actor, director, janr)

            elif search_choice == 3:
                artist_name = input(f"CD izlash uchun uni yozgan artist ismini kiriting: ")
                my_catalog.search_cd(artist_name)

            elif search_choice == 4:
                volume = input(f"Jurnal izlash uchun uni hajmini kiriting, agar bilmasaz enter bosing: ")
                issue = input(f"Yoki uni chop etilgan yilini kiriting, agar bilmasaz enter bosing: ")
                my_catalog.search_magazine(volume, issue)
            else:
                continue

        elif user_choice == 3:
            print(my_catalog.get_catalog_info())

        elif user_choice == 4:
            display_deleting_items()
            while True:
                try:
                    delete_choice = int(input(f"Qaysi buyumni o\'chirasiz? (1-{len(deleting_items_choices)}): "))
                    if delete_choice < 1 or delete_choice > len(deleting_items_choices):
                        raise ValueError(f"Tanlov 1 dan {len(deleting_items_choices)} gacha bo\'lishi shart!")
                    break
                except (TypeError, ValueError) as e:
                    print(f"Xatolik! {e}")

            if delete_choice == 1:
                upc = input("O\'chirmoqchi bo'lgan kitobning UPC raqamini kiriting: ")
                my_catalog.delete_book(upc)

            elif delete_choice == 2:
                upc = input("O\'chirmoqchi bo'lgan DVDning UPC raqamini kiriting: ")
                my_catalog.delete_dvd(upc)

            elif delete_choice == 3:
                artist_name = input("O\'chirmoqchi bo'lgan CD artistining ismini kiriting: ")
                my_catalog.delete_cd(artist_name)

            elif delete_choice == 4:
                volume = int(input("O\'chirmoqchi bo'lgan jurnal hajmini kiriting: "))
                issue = int(input("O\'chirmoqchi bo'lgan jurnal chop etilgan yilini kiriting: "))
                my_catalog.delete_magazine(volume, issue)

            elif delete_choice == 5:
                continue

        elif user_choice == 5:
            break

        else:
            continue

    print("Dastur tugadi.")


main()
