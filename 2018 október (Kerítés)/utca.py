import random
import string

# 1. Feladt
adatok = []
paros = 2
paratlan = 1
fbe = open("kerites.txt")
for sor in fbe:
    sor = sor.strip().split()
    if sor[0] == "0":
        adatok.append([int(sor[0]), int(sor[1]), sor[2], paros])
        paros += 2
    elif sor[0] == "1":
        adatok.append([int(sor[0]), int(sor[1]), sor[2], paratlan])
        paratlan += 2
fbe.close()

# 2. Feladat
print(f"2. feladat\nAz eladott telkek száma: {len(adatok)}\n")

# 3. Feladat
if adatok[-1][0] == 0:
    print(f"3. feladat\nA páros oldalon adták el az utolsó telket.\nAz utolsó telek házszáma: {adatok[-1][3]}\n")
else:
    print(f"3. feladat\nA páratlan oldalon adták el az utolsó telket.\nAz utolsó telek házszáma: {adatok[-1][3]}\n")

# 4. Feladat
paratlan = [x for x in adatok if x[0] == 1]
for i in range(len(paratlan) - 1):
    if paratlan[i][2] not in ["#", ":"]:
        if paratlan[i][2] == paratlan[i + 1][2]:
            break
print(f"4. feladat\nA szomszédossal egyezik a kerítés színe: {paratlan[i][3]}\n")

# 5. Feladat
print("5. feladat")
hazszam = 83  # int(input("5. feladat\nAdjon meg egy házszámot! "))
lehetosegek = list(string.ascii_uppercase)

try:
    lehetosegek.remove(adatok[hazszam-1 - 2][2])
    lehetosegek.remove(adatok[hazszam-1 + 2][2])
except ValueError:
    pass
for i in adatok:
    if i[3] == hazszam:
        print(f"A kerítés színe / állapota: {i[2]}\nEgy lehetséges festési szín: {random.choice(lehetosegek)}")

# 6. Feladat
fki = open("utcakep.txt", "w")
felso_sor = ""
also_sor = ""
hazszam = 1
for i in [x for x in adatok if x[0] == 1]:
    felso_sor += i[2] * i[1]
    also_sor += str(hazszam)
    also_sor += " " * (i[1]-len(str(hazszam)))
    hazszam += 1
print(felso_sor, file=fki)
print(also_sor, file=fki)
fki.close()
