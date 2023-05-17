# 6. Feladathoz
def ertek(darabszam):
    if darabszam == 1:
        return 500
    elif darabszam == 2:
        return 500+450
    elif darabszam == 3:
        return 500+450+400
    else:
        return (500+450) + (darabszam - 3) * 400

# 1. Feladat
adatok = []
gyujto = {}

fbe = open('penztar.txt')
for sor in fbe:
    sor = sor.strip()
    if sor == 'F':
        adatok.append(gyujto)
        gyujto = {}
    else:
        gyujto[sor] = gyujto.get(sor, 0) + 1
fbe.close()

# 2. Feladat
print(f"2. feladat\nA fizetések száma: {len(adatok)}")

# 3. Feladat
print(f"\n3. feladat\nAz első vásárló {sum(adatok[0].values())} árucikket vásárolt")

# 4. Feladat
sorszam = 2  # int(input("\n4. feladat\nAdja meg egy vásárlás sorszámát! "))
nev = "kefe"  # input("Adja meg egy árucikk nevét! ")
db = 2  # int(input("Adja meg a vásárolt darabszámot! "))

# 5. Feladat
kapcs = True
szaml = 0
for i in adatok:
    if nev in i.keys() and kapcs:
        elso = adatok.index(i) + 1
        kapcs = False
    if nev in i.keys():
        utolso = adatok.index(i) + 1
        szaml += 1
print(f"\n5. feladat\n"
      f"Az első vásárlás sorszáma: {elso}\n"
      f"Az utolsó vásárlás sorszáma: {utolso}\n"
      f"{szaml} vásárlás során vettek belőle")

# 6. Feladat
print(f"\n6. feladat\n{db} darab vételekor fizetendő: {ertek(db)}")

# 7. Feladat
print("\n7. feladat")
for k, v in adatok[sorszam-1].items().__reversed__():
    print(v, k)

# 8. Feladat
fki = open("osszeg.txt", "w")
index = 0
for dict in adatok:
    index += 1
    osszeg = 0
    for i in dict.values():
        osszeg += ertek(i)
    print(f"{index}: {osszeg}", file=fki)
fki.close()
