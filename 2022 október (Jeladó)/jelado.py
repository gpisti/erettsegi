import math

#3. Feladat
def eltelt(s1, s2):
    return 3600 * (s2[0] - s1[0]) + 60 * (s2[1] - s1[1]) + (s2[2] - s1[2])


#1. Feladat
adatok = []
fbe = open("jel.txt")
for sor in fbe:
    sor = sor.strip().split()
    adatok.append([int(x) for x in sor])
fbe.close()


#2. Feladat
sorszam = int(input("2. feladat\nAdja meg a jel sorszámát! "))
print(f"x={adatok[sorszam-1][3]}, y={adatok[sorszam-1][4]}")


#4. Feladat
elteltmp = eltelt(adatok[0], adatok[-1])
print(f"\n4. feladat\nIdőtartam: {elteltmp // 3600}"
      f":{(elteltmp % 3600) // 60}"
      f":{(elteltmp % 3600) % 60}")


#5. Feladat
bal = [min([x[3] for x in adatok]), min([x[4] for x in adatok])]
jobb = [max([x[3] for x in adatok]), max([x[4] for x in adatok])]
print(f"\n5. feladat\nBal alsó: {bal[0]} {bal[1]}, jobb felső: {jobb[0]} {jobb[1]}")


#6. Feladat
osszeg = 0
for i in range(len(adatok)):
    try:
        osszeg += math.sqrt(((adatok[i][3] - adatok[i+1][3])**2) + (adatok[i][4] - adatok[i+1][4])**2)
    except IndexError:
        pass
print(f"\n6. feladat\nElmozdulás: {round(osszeg, 3)} egység")


#7. Feladat
fki = open("kimaradt.txt", "w")
for i in range(len(adatok) - 1):
    kimaradt_tavolsag_szerint = 0
    kimaradt_ido_szerint = 0

    idokulonbseg = eltelt(adatok[i], adatok[i + 1])
    if idokulonbseg > 300:
        kimaradt_ido_szerint = (idokulonbseg - 1) // 300

    tavolsag = max(abs(adatok[i + 1][3] - adatok[i][3]), abs(adatok[i + 1][4] - adatok[i][4]))
    if tavolsag > 10:
        kimaradt_tavolsag_szerint = (tavolsag - 1) // 10

    if kimaradt_tavolsag_szerint > kimaradt_ido_szerint:
        print(f"{adatok[i + 1][0]} {adatok[i + 1][1]} {adatok[i + 1][2]}"
              f" koordináta-eltérés kimaradt_tavolsag_szerint", file=fki)
    if kimaradt_tavolsag_szerint <= kimaradt_ido_szerint != 0:
        print(f"{adatok[i + 1][0]} {adatok[i + 1][1]} {adatok[i + 1][2]}"
              f" időeltérés kimaradt_ido_szerint", file=fki)

fki.close()