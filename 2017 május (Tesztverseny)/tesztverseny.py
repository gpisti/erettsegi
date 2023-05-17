# 1. Feladat
adatok = []
megoldas = None
fbe = open("valaszok.txt")
for sor in fbe:
    sor = sor.strip().split()
    try:
        adatok.append([sor[0], sor[1]])
    except IndexError:
        megoldas = ''.join(sor)
print("1. feladat: Az adatok beolvasása\n")

# 2. Feladat
print(f"2. feladat: A vetélkedőn {len(adatok)} versenyző indult.\n")

# 3. Feladat
azonosito = "AB123"  # input("3. feladadt: A versenyző azonosítója = ")
print(f"{''.join([x[1] for x in adatok if x[0] == azonosito])}\t(a versenyző válasza)\n")

# 4. Feladat
print(f"4. feladat:\n{''.join(megoldas)}\t(a helyes megoldás)")
for i in range(len(megoldas)):
    if [x[1] for x in adatok if x[0] == azonosito][0][i] == megoldas[i]:
        print("+", end="")
    else:
        print(" ", end="")
print()
print()

# 5. Feladat
sorszam = 10 - 1  # int(input("5. feladat: A feladat sorszáma = ")) - 1
ossz = len([x for x in adatok if x[1][sorszam] == megoldas[sorszam]])
print(f"A feladatra {ossz} fő, a versenyzők {round(ossz / len(adatok) * 100, 2)}%-a adott helyes \nválaszt.\n")

# 6. Feladat
fki = open("pontok.txt", "w")
pont = 0
for i in adatok:
    for j in range(len(megoldas)):
        if i[1][j] == megoldas[j]:
            if j <= 5:
                pont += 3
            elif j >= 6 and j <= 10:
                pont += 4
            elif j >= 11 and j <= 13:
                pont += 5
            else:
                pont += 6
    print(i[0], pont, file=fki)
    pont = 0
print("6. feladat: A versenyzők pontszámának meghatározása\n")
fki.close()

# 7. Feladat
legjobbak = {}
fbe = open("pontok.txt")
for sor in fbe:
    sor = sor.strip().split()
    legjobbak[sor[0]] = int(sor[1])
fbe.close()

top3 = sorted(set(legjobbak.values()), reverse=True)[:3]
for i in range(3):
    for k, v in legjobbak.items():
        if v == top3[i]:
            print(f"{i+1}. díj ({top3[i]} pont): {k}")
