# 4. Feladat
def ado(sav, terulet):
    if adosav[sav] * terulet >= 10000:
        return adosav[sav] * terulet
    else:
        return 0

# 1. Feladat
adatok = []
fbe = open("utca.txt")
for sor in fbe:
    sor = sor.strip().split()
    try:
        adatok.append([int(sor[0]), sor[1], sor[2], sor[3], int(sor[4])])
    except IndexError:
        adosav1 = list(map(int, sor))
        adosav = {"A": adosav1[0],
                  "B": adosav1[1],
                  "C": adosav1[2]}
fbe.close()


# 2. Feladat
print(f"2. feladat. A mintában {len(adatok)} telek szerepel.")


# 3. Feladat
print("3. feladat")
adoszam = 68396  # int(input("3. feladat. Egy tulajdonos adószáma: "))
for i in adatok:
    if i[0] == adoszam:
        print(f"{i[1]} utca {i[2]}")


# 5. Feladat
print("5. feladat")
savok = {}
for i in adatok:
    if i[3] not in savok:
        savok[i[3]] = [0, 0]
    if i[3] in savok:
        savok[i[3]][0] += ado(i[3], i[-1])
        savok[i[3]][1] += 1
for k, v in sorted(savok.items()):
    print(f"{k} sávba {v[1]} telek esik, az adó {v[0]} Ft. ")


# 6. Feladat
print("6. feladat. A több sávba sorolt utcák:")
utcak = {}
for i in adatok:
    if i[1] not in utcak:
        utcak[i[1]] = []
    if i[1] in utcak:
        utcak[i[1]].append(i[3])

for k, v in utcak.items():
    if len(v) != v.count(v[0]):
        print(k)


# 7. Feladat
fki = open("fizetendo.txt", "w")
fizetendo = {}
for i in adatok:
    if i[0] not in fizetendo:
        fizetendo[i[0]] = 0
    if i[0] in fizetendo:
        fizetendo[i[0]] += ado(i[3], i[-1])
for k, v in fizetendo.items():
    print(k, v, file=fki)
fki.close()
