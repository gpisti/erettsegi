from random import choice


def dobas():
    return choice(choice(["F", "I"]))


# 1. Feladat
print(f"1. feladat\nA pénzfeldobás eredménye: {dobas()}")

# 2. Feladat
print("2. feladat")
tipp = "I"  # input("2. feladat\nTippelj! ")
eredmeny = dobas()
print(f"A tipp {tipp}. a dobás eredménye {eredmeny} volt.")
if eredmeny == tipp:
    print("Ön eltalálta!")
else:
    print("Ön nem találta el!")

# 3. feladat
szaml = 0
fbe = open("kiserlet.txt")
for i in fbe:
    szaml += 1
fbe.close()
print(f"3. feladat\nA kísérlet {szaml} dobásból állt.")

# 4. Feladat
fej = 0
fbe = open("kiserlet.txt")
for i in fbe:
    if i.strip() == "F":
        fej += 1
print(f"4. feladat\nA kísérlet során a fej relatív gyakorisága {round(fej / szaml * 100, 2)}% volt.")
fbe.close()

# 5. Feladat
dupla, fej, iras = 0, 0, 0
leghosszabb, index, szaml = 0, 0, 0  # 6. feladathoz
fbe = open("kiserlet.txt")
for i in fbe:
    szaml += 1
    i = i.strip()
    if i == "F":
        fej += 1
    if i == "I":
        if fej == 2:
            dupla += 1
        if leghosszabb < fej:
            leghosszabb = fej
            index = szaml - fej
        fej = 0
print(f"5. feladat\nA kísérlet során {dupla} alkalommal dobtak pontosan két fejet egymás után.")
fbe.close()

# 6. Feladat
print(f"6. feladat\nA leghosszabb tisztafej sorozat {leghosszabb} tagból áll. kezdete a(z) {index}. dobás.")

# 7. Feladat
fki = open("dobasok.txt", "w")
dobasok = [f"{dobas()}{dobas()}{dobas()}{dobas()}" for x in range(250)]
FFFF, FFFI = 0, 0
for i in dobasok:
    if i == "FFFF":
        FFFF += 1
    if i == "FFFI":
        FFFI += 1
print(f"FFFF: {FFFF}, FFFI: {FFFI}\n{' '.join(dobasok)}", file=fki)
fki.close()
