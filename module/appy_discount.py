# from constant import summa


def apply_discount(summa: int) -> int:
    j = input("PROMOKOD KIRITASIZMI: ha/ yoq: ")
    total = summa
    if j == 'ha' or j == 'HA':
        promokod = input("PROMOKODNI KIRITING: ")
        if promokod == 'uz24':
            print("PROMOKOD QABUL QILINDI, 30 FOYZ CHEGIRMA")
            pn = summa / 10
            pn *= 3
            total = summa - pn
            print("TOTAL, CHEGIRMA BILAN -", total)
    return total


print(apply_discount(12000))
