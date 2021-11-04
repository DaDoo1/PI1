#vek = int(input("zadaj svoj vek: "))
#print(vek + 10)

#polomerKruhu = float(input("zadaj polomer kruhu: "))
#obvodkruhu = 2*3.14*polomerKruhu
#print("obvod kruhu je", obvodkruhu)

"""
a = int(input("zadaj a: "))
b = int(input("zadaj b: "))
print("scitanie:", a + b)
print("odcitanie:", a - b)
print("nasobenie:", a * b)
if b == 0:
    print("nulou sa delit neda")
else:
    print("delenie:", a / b)
"""


#+-, *, %, **, /                - aritmeticke operatory
#==, !=, <, >, <=, >=           - logicke operatory
#vysledok = 1 != 2
#print(vysledok)

"""
vek = int(input("zadaj svoj vek: "))
if vek >= 18:
    print("mas dost rokov, vstup dalej")
    print("vitaj medzi nami")
else:
    print("vstup zakazany, si moc mlady")
print("tento kod sa vykona vzdy")
"""

"""
day = 5
hour = 12
if day == 1:
    print("pondelok")
elif day == 2:
    print("utorok")
elif day == 3:
    print("streda")
elif day == 4:
    print("stvrtok")
elif day == 5:
    print("piatok")
    if hour < 12:
        print("je doobeda")
    else:
        print("je poobede")
elif day == 6:
    print("sobota")
elif day == 7:
    print("nedela")
"""

""""
username = input ("zadaj prihlasovacie meno: ")
password = input ("zadaj prihlasovacie heslo: ")
vek = input("zadaj svoj vek: ")
if username == "root" and password == "password" and vek == "18":
    print("uspesne si sa prihlasil!")
else:
    print("zle meno alebo heslo alebo
"""
""""
cislo = 1
while (cislo <= 10)
print(cislo)
cislo = cislo
"""

"""""
start = 10
koniec = 0
while start >= koniec:
    if start == 5:
        start -= 1
    continue
    print(start)
    start -= 1

start = 10
while start >= koniec:
    if start == 5:
        break
    print(start)
    start -= 1
"""""

"""""
start = int(input("Zadaj odkial začnem počítat"))
koniec = int(input("Zadaj pokial budem pocitat"))
while(start < koniec):
    if(start % 3 == 0):
        print(start, "je nasobok 3ky")
    start += 1
 """""
"""""
for premena in range(10)
    print(premena)
"""""

"""""
cislo = "123456789"
spoluhlasky = "dtnlkghchďťňľčšdzdžžjbmprvzsf"
samohlasky = "aáeéiíouúyý"
slovo = input("zadajte slovo")
pocet_spoluhlasok = 0
pocet_samohlasok = 0
pocet_cisel = 0
pocet_znakov = 0
for znak in slovo:
     if znak in samohlasky:
        pocet_samohlasok += 1
     if znak in spoluhlasky:
        pocet_spoluhlasok += 1
     if znak in cislo:
        pocet_cisel += 1
     else:
        pocet_znakov +=1



if pocet_znakov > 0:
    print("slovo obsahuje ine znaky" , pocet_znakov)
else:
    print("slovo neobsahuje ine znaky")



if pocet_cisel > 0:
    print("slovo obsahuje cislo" , pocet_cisel)
else:
    print("slovo neobsahuje cislo")

if pocet_spoluhlasok > 0:
    print("slovo obsahuje spoluhlasky" , pocet_spoluhlasok)
else:
    print("slovo neobsahuje samohlasku")


if pocet_samohlasok > 0:
    print("slovo obsahuje samohlasky", pocet_samohlasok)
else:
    print("slovo neobsahuje spoluhlasku")
"""


















