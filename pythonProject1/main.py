def koniec():
    if otazka == "koniec":
        return True
    else:
        return False


while True:
    pocitadlo = 0

    print("A - Fico")
    print("B - Tesla")
    print("C - Gates")
    print("D - Musk")

    otazka = input("kto vynasiel teslu ? ")

    if koniec():
        break

    if otazka.lower() == "d":
        print("mas to dobre presiel si")
        pocitadlo += 1
    else:
        print("zadal si zlu odpoved")
        pocitadlo -= 1

    print("A - 24")
    print("B - 15")
    print("C - 6")
    print("D - 48")

    otazka2 = input("Kolko hodin ma den? ")

    if otazka2 == "koniec":
        break

    if otazka2.lower() == "a":
        print("mas to dobre")
        pocitadlo += 1
    else:
        print("nemas to dobre")
        pocitadlo -= 1

    print("Quiz skoncil, pocet spravnych odpovedi:", pocitadlo)
    break
