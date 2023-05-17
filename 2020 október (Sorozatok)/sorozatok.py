# 6. Feladat
def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev -1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]
    return hetnapja


# 1. Feladat
gyujto = []
adatok = []
fbe = open("lista.txt")
for sor in fbe:
    gyujto.append(sor.strip())
    if len(gyujto) == 5:
        adatok.append(gyujto)
        gyujto = []
fbe.close()

# 2. Feladat
print(f"2. feladat"
      f"\nA listában {len(adatok) - [x[0] for x in adatok].count('NI')} db vetítési dátummal rendelkező epizód van.\n")

# 3. Feladat
print(f"3. feladat"
      f"\nA listában lévő epizódok {round(len([x[4] for x in adatok if x[4] == '1']) / len(adatok) * 100, 2)}%-át látta.\n")

# 4. Feladat
m = sum([int(x[3]) for x in adatok if x[4] == '1'])
print(f"4. feladat"
      f"\nSorozatnézéssel {m // 1440} napot {m % 1440 // 60} órát és {m - ((m // 1440) * 1440) - ((m % 1440 // 60) * 60)} percet töltött.\n")

# 5. Feladat
datum = input("5. feladat\nAdjon meg egy dátumot! Dátum= ")
datum = int(datum[:4]+datum[5:7]+datum[8:])
datumadatok = {}
for i in adatok:
    if i[0] != "NI" and i[4] == "0":
        datumadatok[int(i[0][:4] + i[0][5:7] + i[0][8:])] = [i[2], i[1]]
for k, v in datumadatok.items():
    if k <= datum:
        print(*v)
print()

# 7. Feladat
nap = input("7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ")
vetitettek = set()
kapcs = True
for i in adatok:
    if i[0] != "NI":
        if hetnapja(int(i[0][:4]), int(i[0][5:7]), int(i[0][8:])) == nap:
            vetitettek.add(i[1])
            kapcs = False
if kapcs:
    print("Az adott napon nem kerül adásba sorozat.")
else:
    for i in vetitettek:
        print(i)

# 8. Feladat
fki = open("summa.txt", "w")
sorozatok = {}
for i in adatok:
    if i[1] in sorozatok:
        sorozatok[i[1]][0] += int(i[3])
        sorozatok[i[1]][1] += 1
    if i[1] not in sorozatok:
        sorozatok[i[1]] = [int(i[3]), 1]
for k, v in sorozatok.items():
    print(k, *v, file=fki)
fki.close()