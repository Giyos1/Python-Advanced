from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    filename="library.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger("Library")


# logger.debug("ishladi!!")
# logger.info("loggerni sinash")
#
#
# def sum(a, b):
#     # print("info, ikkta soni yigindisi uchun logger ishladi")
#     logger.info("info, ikkta soni yigindisi uchun logger ishladi")
#     # print(a)  # debug
#     logger.debug(a)
#     # print(b)  # debug
#     logger.debug(b)
#     logger.info(a + b)
#     return a + b
#
#
# sum(12, 24)


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
        logger.debug(f"{self.title},{self.subject}, otasidagi __init ishladi")
        logger.info(f"{self.__item} ta item boldi library da")

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

    def __str__(self):
        return self.title


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
    def __init__(self):
        self.items = []

    def add_item(self, item: LibraryItem):
        # if isinstance(item, LibraryItem):
        #     self.items.append(item)
        # else:
        #     logger.error(f"{item} boshqa malumot typega kiradi {type(item).__name__}")
        # print(self.items[0])
        logger.debug(f"{type(item).__name__} classiga tegishli")
        if isinstance(item, LibraryItem):
            self.items.append(item)
        else:
            logger.critical(f"{item} boshqa malumot typega kiradi {type(item).__name__}")
            raise ValueError("boshqa malumot turi")
        return item

    def search(self, keyword):
        found_items = []
        # if not keyword:
        #     logger.warning("search functionga key berilmadi")

        for i in self.items:
            if keyword.lower() in i.title.lower():
                found_items.append(i)
        if not found_items:
            logger.warning(f"{keyword} nomli item yoq ekan shundan ketirish kerak")
        return found_items


cd = CD("asas", "asas")
print(cd.title)

c = Catalog()
c.add_item(cd)
c.search("asdasdasdsadsa")
c.add_item(cd)
