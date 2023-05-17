# 1. Feladat
adatok = []
fbe = open("tavirathu13.txt")
for sor in fbe:
    sor = sor.strip().split()
    adatok.append([sor[0], int(sor[1][:2]), int(sor[1][2:]), sor[2], sor[3]])
fbe.close()

# 2. Feladat
kod = "SM"  # input("2. feladat\nAdja meg egy település kódját! Település: ")
print(f"Az utolsó mérési adat a megadott településről {adatok[-1][1]}:{adatok[-1][2]}-kor érkezett")

# 3. Feladat
for i in adatok:
    if i[4] == min([x[4] for x in adatok]):
        minc, minh, minm, mint = i[0], i[1], i[2], i[4]
    if i[4] == max([x[4] for x in adatok]):
        maxc, maxh, maxm, maxt = i[0], i[1], i[2], i[4]

print(f"3. feladat"
      f"\nA legalacsonyabb hőmérséklet: {minc} {minh}:{minm} {mint} fok."
      f"\nA legmagasabb hőmérséklet: {maxc} {maxh}:{maxm} {maxt} fok.")

# 4. Feladat
print("4. feladat")
for i in adatok:
    if i[3] == "00000":
        print(f"{i[0]} {str(i[1]).zfill(2)}:{str(i[2]).zfill(2)}")

# 5. Feladat
print("5. feladat")
khomersekletek = {}
ihomersekletek = {}
eredmeny = {}

for i in adatok:
    if i[0] in khomersekletek and i[1] in [1, 7, 13, 19]:
        khomersekletek[i[0]].append(int(i[4]))
    if i[0] not in khomersekletek and i[1] in [1, 7, 13, 19]:
        khomersekletek[i[0]] = [int(i[4])]

    if i[0] in ihomersekletek:
        ihomersekletek[i[0]].append(int(i[4]))
    if i[0] not in ihomersekletek:
        ihomersekletek[i[0]] = [int(i[4])]

for k, v in khomersekletek.items():
    eredmeny[k] = [sum(v) // len(v)]
for k, v in ihomersekletek.items():
    eredmeny[k].append(max(v)-min(v))
for k, v in eredmeny.items():
    print(f"{k} Középhőmérséklet: {v[0]}; Hőmérséklet-ingadozás: {v[1]}")


# 6. Feladat
print("6. feladat\nA fájlok elkészültek.")
for i in list(sorted(set(x[0] for x in adatok))):
    fki = open(f"{i}.txt", "w")
    print(i, file=fki)
    for j in adatok:
        if j[0] == i:
            print(f"{str(j[1]).zfill(2)}:{str(j[2]).zfill(2)} {'#' * int(j[3][3:])}", file=fki)
    fki.close()
