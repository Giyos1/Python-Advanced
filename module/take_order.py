# from main import summa, zakazlar


def take_order():
    summa = 0
    zakaz = True
    zakazlar = {}
    while zakaz:
        menyu = {
            'lagmon': 20000,
            'osh': 25000,
            'manti': 15000,
            'shashlik': 10000
        }
        ovqat = input("ZAKAZINGIZNI KIRITING: ")
        for key, value in menyu.items():
            if key == ovqat:
                print("ZAKAZINGIZ QABUL QILINDI")
                summa += value
                print(summa)
                zakazlar[key] = value
                yana = input("YANA ZAKAZ BERASIZMI? ha/yoq - ")
                if yana == 'ha' or yana == 'HA':
                    continue
                else:
                    zakaz = False

    return summa, zakazlar


if __name__ == '__main__':
    # take_order()
    # print(summa)
    # print(zakazlar)
    pass
