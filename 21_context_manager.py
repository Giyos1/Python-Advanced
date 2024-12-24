# try:
#     file = open("data.txt", "r")
#     file1 = file.read()
#     print(file1)
#     1/0
# finally:
#     file.close()
#     print("closed file")


# class MyContextManager:
#     def __enter__(self):
#         print("context manager ishladi")
#         return "context manager"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("context managerdan chiqyapmiz")
#
#         if exc_type:
#             print(f"{exc_val} shunaqangi xato")
#         return True
#
#
# with MyContextManager() as context:
#     print(context)
#     raise ValueError("custom")
#
# print(1+2)
#
# class File:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = open(self.filename, self.mode)
#
#     def __enter__(self):
#         print("context yuklandi")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             print("file closed")
#             self.file.close()
#
#
# with File("data.txt", "r") as fayl:
#     fayl1 = fayl.read()
#     print(fayl1)

import csv

data = [
    {"ism": "ali", "yoshi": 21, "bosqich": 1, "ingliz": 5},
    {"ism": "ali", "yoshi": 21, "bosqich": 1, "ingliz": 5},
    {"ism": "ali", "yoshi": 21, "bosqich": 1, "ingliz": 5}
]


def write(data):
    with open("data.csv", "w", newline="") as fayl:
        main = ["ism", "yoshi", "bosqich", "ingliz"]
        w = csv.DictWriter(fayl, fieldnames=main)
        w.writeheader()
        w.writerows(data)


def read():
    with open("data.csv", "r") as fayl:
        reader = csv.reader(fayl)
        for i in reader:
            print(i)


# talabalar_soni = 0
# talabalar_yoshi = 0
# with open("data.csv", "r") as fayl:
#     reader = csv.DictReader(fayl)
#     answer = input("ingliz tili fanidagi baxolarni kormoqchimiz>>>(ha/yoq)")
#     if answer.lower() == "ha":
#         for i in reader:
#             print(f'{i.get("ism")} talaba ingliz tilidan {i.get("ingliz")}')
#
#         # talabalar_soni += 1
#         # talabalar_yoshi += int(i.get("yoshi", 0))
#     # print("ortacha yoshi", talabalar_yoshi / talabalar_soni)

# talaba_dict = {"ism": "vali", "yoshi": 21, "bosqich": 1, "ingliz": 5}
# data.append(talaba_dict)
#
# write(data)
# read()

# import json
#
# talaba = {"ism": "ali", "yoshi": 21, "bosqich": 1, "ingliz": 5}
#
# with open("talaba.json", "w") as fayl:
#     fayl = json.dump(talaba, fayl, indent=4)
#
# with open("talaba.json", "r") as fayl:
#     dat1 = json.load(fayl)
# print(dat1)


