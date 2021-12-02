"""
from random import randint
privlastky = ["maly", "velky", "pekny", "skaredy", "chudy", "tucny", "vesely", "smutny", "nudny", "zaujimavy"]
zoznamMien = []

while True:
    meno = input("zadaj meno: ")
    priezvisko = input("zadaj priezvisko: ")


    mismas = meno + " " +privlastky[randint(0,9)] + " " + priezvisko
    print(mismas)
    zoznamMien.append(mismas)

    print(zoznamMien)


    for i in range(1, len(zoznamMien)+1):
        print(str(i+1)+"x.\t" + zoznamMien[i])
"""




import random
tym1 = []
tym2 = []
tym3 = []

while True:
    nick = input("zadaj svoju prezývku:")
    tym = random.randrange(0, 3)
    if tym == 0:
        tym1.append(nick)
    elif tym == 1:
        tym2.append(nick)
    elif tym == 2:
        tym3.append(nick)
    print("v tyme 1 sú:", tym1)
    print("v tyme 2 sú:", tym2)
    print("v tyme 3 sú:", tym3)








