def display_menu():
    print("""
    MENU:
    1. OSH - 25 000 SOM
    2. MANTI - 15 000 SOM
    3. LAGMON - 20 000 SOM
    4. SHASHLIK - 10 000 SOM
    """)

summa = 0
zakazlar = {}
def take_order():
    global summa
    zakaz = True
    global zakazlar
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
                zakazlar[key] = value
                yana = input("YANA ZAKAZ BERASIZMI? ha/yoq - ")
                if yana == 'ha' or yana == 'HA':
                    continue
                else:
                    zakaz = False

def calculate_total():
    total = 0
    total += summa
    print("ZAKAZLARINGIZ -", zakazlar)
    print("SIZNI TOTAL BUYURTMANGIZ NARXI -", total)

def apply_discount():
    j = input("PROMOKOD KIRITASIZMI: ha/ yoq: ")
    if j == 'ha' or j == 'HA':
        promokod = input("PROMOKODNI KIRITING: ")
        if promokod == 'uz24':
            print("PROMOKOD QABUL QILINDI, 30 FOYZ CHEGIRMA")
            pn = summa / 10
            pn *= 3
            total = summa - pn
            print("TOTAL, CHEGIRMA BILAN -", total)

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
                    display_menu()
                case 2:
                    take_order()
                    if summa != 0:
                        calculate_total()
                case 3:
                    apply_discount()
                case 4:
                    restoran = False
    except:
        print("FAQAT 1 va 4 ORALIGIDA KIRITING!")
        break
