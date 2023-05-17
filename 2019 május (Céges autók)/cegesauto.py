# 1. Feladat
adatok = []
fbe = open("autok.txt")
for sor in fbe:
    sor = sor.strip().split()
    adatok.append([int(sor[0]), int(sor[1][:2]), int(sor[1][3:]), sor[2], int(sor[3]), int(sor[4]), int(sor[5])])
fbe.close()

# 2. Feladat
print(f"2. feladat\n {adatok[-1][0]}. nap rendszám: {adatok[-1][3]}")

# 3. Feladat
nap = int(input("3. feladat\nNap: "))
print(f"Forgalom a(z) {nap}. napon:")
for i in adatok:
    if i[0] == nap and i[-1] == 0:
        print(f"{str(i[1]).zfill(2)}:{str(i[2]).zfill(2)} {i[3]} {i[4]} ki")
    if i[0] == nap and i[-1] == 1:
        print(f"{str(i[1]).zfill(2)}:{str(i[2]).zfill(2)} {i[3]} {i[4]} be")

# 4. Feladat
garazsban = [x[3] for x in adatok]
for i in adatok:
    if i[-1] == 0:
        garazsban.remove(i[3])
    if i[-1] == 1:
        garazsban.append(i[3])
print(f"4. feladat\nA hónap végén {len(adatok) - len(garazsban)} autót nem hoztak vissza.")

# 5. Feladat
print("5. feladat")
autok = {}
for i in adatok:
    if i[3] in autok:
        autok[i[3]].append(i[5])
    if i[3] not in autok:
        autok[i[3]] = [i[5]]
for k, v in sorted(autok.items()):
    print(f"{k} {v[-1] - v[0]} km")

# ---------- #
# 6. Feladat
# ---------- #

# 7. Feladat
rendszam = input("7. feladat\nRendszám: ")
fki = open(f"{rendszam}.txt", "w")
for i in adatok:
    if i[3] == rendszam and i[-1] == 0:
        print(f"{i[4]}\t{i[0]}. {str(i[1]).zfill(2)}:{str(i[2]).zfill(2)}\t{i[5]}\t", end="", file=fki)
    if i[3] == rendszam and i[-1] == 1:
        print(f"{i[0]}. {str(i[1]).zfill(2)}:{str(i[2]).zfill(2)}\t{i[5]} km", file=fki)
fki.close()
