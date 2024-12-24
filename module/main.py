from display_menu import display_menu as d
from take_order import take_order
from calculate import calculate_total
from appy_discount import apply_discount

# from constant import summa
summa = 0
zakazlar = {}


def main():
    global zakazlar
    global summa
    restoran = True
    while restoran:
        print("""
        1. MENYUNI KORISH
        2. ZAKAZ BERISH
        3. PROMOKOD KIRITISH
        4. DASTURNI TOXTATSH
        """)
        choice = int(input("TANLOVINGIZNI KIRITING: "))
        try:
            if 1 > choice and choice > 4:
                raise ValueError
            else:
                match choice:
                    case 1:
                        d()
                    case 2:
                        summa, zakazlar = take_order()
                        print(summa)
                        if summa != 0:
                            calculate_total(summa, zakazlar)
                    case 3:
                        apply_discount(summa)
                    case 4:
                        restoran = False
        except:
            print("FAQAT 1 va 4 ORALIGIDA KIRITING!")
            break


main()
