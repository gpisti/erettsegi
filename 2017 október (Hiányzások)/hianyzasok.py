# 4. Feladat
def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1]+nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja

# 1. Feladat
adatok = []
fki = open('naplo.txt')
for sor in fki:
    sor = sor.strip().split()
    if sor[0] == '#':  # dátumot találtunk
        honap = int(sor[1])
        nap = int(sor[2])
    else:  # hiányzás-bejegyzést találtunk
        vezeteknev = sor[0]
        keresztnev = sor[1]
        hianyzas = sor[2]
        adatok.append([honap, nap, f"{vezeteknev} {keresztnev}", hianyzas])
fki.close()

# 2. Feladat
print(f"A naplóban {len(adatok)} bejegyzés van.")

# 3. Feladat
osszhiany = "".join([x[3] for x in adatok])

print(f"3. feladat\nAz igazolt hiányzások száma {osszhiany.count('X')}, az igazolatlanoké {osszhiany.count('I')} óra. ")

# 5. Feladat
honap = int(input("5. feladat\nA hónap sorszáma="))
nap = int(input("A nap sorszáma="))
print(f"Azon a napon {hetnapja(honap, nap)} volt.")

# 6. Feladat
nap = input("6. feladat\nA nap neve=")
sorszam = int(input("Az óra sorszáma="))
szaml = 0
for i in adatok:
    if hetnapja(i[0], i[1]) == nap:
        if i[-1][sorszam-1] in ["X", "I"]:
            szaml += 1
print(f"Ekkor összesen {szaml} óra hiányzás történt.")

# 7. Feladat
print(f"7. feladat\nA legtöbbet hiányzó tanulók: ", end="")
tophianyzok = {}
for i in adatok:
    if i[2] in tophianyzok:
        tophianyzok[i[2]] += len(i[3]) - i[3].count("O")
    if i[2] not in tophianyzok:
        tophianyzok[i[2]] = len(i[3]) - i[3].count("O")
index = 0
top3 = sorted(tophianyzok.values(), reverse=True)[:3]
for k, v in tophianyzok.items():
    if v == top3[index]:
        print(f"{k}, ", end="")
        index += 1
    if index > 3:
        break
