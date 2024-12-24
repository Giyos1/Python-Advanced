from datetime import datetime

a = 12
b = 15
print(a > b)


# print(abs(a))
class Unversitet:
    def __init__(self, name: str) -> None:
        self.name = name
        self.talabalar = [Talaba("giyos", 21)]
        self.n = 1

    def get_info(self) -> str:
        return self.name

    # def __str__(self):
    #     return "1"

    def __repr__(self) -> str:
        return self.name

    def __gt__(self, other: "Unversitet") -> bool:
        return len(self.talabalar) > len(other.talabalar)

    def __ne__(self, other: "Unversitet") -> bool:
        return len(self.talabalar) != len(other.talabalar)

    def __eq__(self, other):
        return len(self.talabalar) == len(other.talabalar)

    def __len__(self) -> int:
        return len(self.talabalar)

    def __getitem__(self, index:int)->"Talaba":
        return self.talabalar[index]

    def __setitem__(self, index, talaba: "Talaba")->"Talaba":
        self.talabalar[index] = talaba
        return self.talabalar[index]

    def __add__(self, other):
        if isinstance(other, Unversitet):
            new_unversite = Unversitet(f"{self.name} va {other.name}")
            new_unversite.talabalar = self.talabalar + other.talabalar
            return new_unversite
        return "siz Unversitet objectini bermadiz"

    def __sub__(self, other):
        if isinstance(other, Unversitet):
            new_unversite = Unversitet(f"{self.name} va {other.name}")
            new_unversite.talabalar = len(self.talabalar) - len(other.talabalar)
            return new_unversite
        return "siz Unversitet objectini bermadiz"

    def __call__(self, *args, **kwargs):
        return self.name


class Talaba:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __gt__(self, other: "Talaba") -> bool:
        return self.grades > other.grades

    def __repr__(self):
        return f"{self.name}, {self.grades}"


today = datetime.now()

u1 = Unversitet("TATU")
print(u1)
u2 = Unversitet("ISFT")
print(u1 == u2)

print(len(u1))
print(u1[0])
u1[0] = Talaba("asas", 12)
print(u1[0])

u3 = u1 - u2
print(u3.talabalar)

print(u1())
