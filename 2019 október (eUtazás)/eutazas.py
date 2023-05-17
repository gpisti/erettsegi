# 6. Feladat
def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    napokszama = d2 - d1
    return napokszama


# 1. Feladat
adatok = []
fbe = open("utasadat.txt")
for sor in fbe:
    sor = sor.strip().split()
    adatok.append([int(sor[0]), int(sor[1][:8]), int(sor[1][9:11]), int(sor[1][11:]), int(sor[2]), sor[3], int(sor[4])])
fbe.close()

# 2. Feladat
print(f"2. feladat\nA buszra {len(adatok)} utas akart felszállni.")

# 3. Feladat
szaml = 0
for i in adatok:
    if i[5] != "JGY" and i[6] < i[1]:
        szaml += 1
    if i[5] == "JGY" and i[6] == 0:
        szaml += 1
print(f"3. feladat\nA buszra {szaml} utas nem szállhatott fel. ")

# 4. Feladat
megallok = {}
for i in adatok:
    if i[0] in megallok:
        megallok[i[0]] += 1
    if i[0] not in megallok:
        megallok[i[0]] = 1
for k, v in megallok.items():
    if v == max(megallok.values()):
        print(f"4. feladat\nA legtöbb utas ({v} fő) a {k}. megállóban próbált felszállni. ")
        break

# 5. Fealdat
kedvezmeny = 0
ingyen = 0
for i in adatok:
    if i[5] in ["TAB", "NYB"] and i[1] <= i[6]:
        kedvezmeny += 1
    if i[5] in ["NYP", "RVS", "GYK"] and i[1] <= i[6]:
        ingyen += 1
print(f"5. feladat\nIngyenesen utazók száma: {ingyen} fő\nA kedvezményesen utazók száma: {kedvezmeny} fő")

# 7. Feladat
fki = open("figyelmeztetes.txt", "w")
for i in adatok:
    if i[5] != "JGY":
        i[1] = str(i[1])
        i[6] = str(i[6])
        maradek = napokszama(int(i[1][:4]), int(i[1][4:6]), int(i[1][6:]), int(i[6][:4]), int(i[6][4:6]), int(i[6][6:]))
        if 0 < maradek < 4:
            print(f"{str(i[4])} {str(i[6][:4])}-{str(i[6][4:6])}-{str(i[6][6:])}", file=fki)
fki.close()
