from queries import *

def menu():
    while True:
        print("""
1 - Okresy
2 - Obce v okrese
3 - Hledat obec
4 - Statistiky
0 - Konec
""")

        volba = input("Vyber: ")

        if volba == "1":
            vypis_okresu()
        elif volba == "2":
            obce_v_okrese()
        elif volba == "3":
            hledani_obce()
        elif volba == "4":
            statistika_okresu()
        elif volba == "0":
            break
        else:
            print("Špatně")

menu()