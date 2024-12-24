import pickle
from abc import ABC, abstractmethod


class Author:
    def __init__(self, name):
        self.name = name


class LibraryItem(ABC):
    __item = 0  # incapsulation

    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject
        LibraryItem.__item += 1

    @classmethod
    def get_items(cls):
        return cls.__item

    @abstractmethod  # abstraction
    def locate(self):
        pass

    @abstractmethod  # abstraction
    def get_info(self):
        pass

    def __str__(self):
        return self.title


class Book(LibraryItem):
    def __init__(self, isbn, dds_num, title, upc, subject):
        super().__init__(title, upc, subject)
        self.isbn = isbn
        self.dds_number = dds_num
        self.authors = []

    def set_authors(self, author: Author):
        pass

    def locate(self):
        return self.dds_number

    def get_info(self):
        return f"{self.title} {self.subject}"

    def __str__(self):
        return self.title


class DVD(LibraryItem):
    def __init__(self, janr, actors, title):
        super().__init__(title, upc=None, subject=None)
        self.janr = janr
        self.actors = actors

    def locate(self):
        return self.janr + " " + self.title

    def get_info(self):
        return f"{self.title} {self.subject}"


class CD(LibraryItem):
    def __init__(self, author, title):
        super().__init__(title, upc=None, subject=None)
        self.author = author

    def locate(self):
        return self.title + " " + self.author

    def get_info(self):
        return f"{self.author} {self.title},{self.upc}"


class Magazine(LibraryItem):
    def __init__(self, volume, issue, title):
        super().__init__(title, upc=None, subject=None)
        self.volume = volume
        self.issue = issue

    def locate(self):
        return self.title + " " + self.volume + " " + self.issue

    def get_info(self):
        return f"{self.title} {self.volume},{self.upc}"


class Catalog:
    def __init__(self, name):
        self.items = []
        self.name = name

    def add_item(self, item: LibraryItem):
        self.items.append(item)
        return item

    def search(self, keyword):
        found_items = []
        for i in self.items:
            if keyword.lower() in i.title.lower():
                found_items.append(i)
        return found_items

    def __str__(self):
        return f"{self.name}, {[i.title for i in self.items]}"


def read_file():
    catalog1 = None
    try:
        with open("library.dat", "rb") as fayl:
            catalog1 = pickle.load(fayl)
    except Exception as e:
        print("exept", e)
    return catalog1


def write_file(catalog1, args):
    with open("library.dat", "wb") as fayl:
        if not catalog1:
            catalog1 = Catalog("yangi kutubxona")
        for i in args:
            if isinstance(i, CD):
                catalog1.add_item(i)
        pickle.dump(catalog1, fayl)


def main():
    while True:
        print("""
       1.Catolog malumotlarini korish
       2.CD qoshish
       3.chiqish
       """)
        catalog = read_file()
        choices = int(input("menu ni tanlang"))
        if choices == 1:
            print(catalog)
        elif choices == 2:
            cd_list = []
            while True:
                title = input("cd ni  titleni kiriting>>")
                author = input("authorni kiritng>>")
                cd = CD(title, author)
                cd_list.append(cd)
                choice = input("davom etamizmi??")
                if choice == "yoq":
                    break
            write_file(catalog, cd_list)
        else:
            break


if __name__ == '__main__':
    main()
