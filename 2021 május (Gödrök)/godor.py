# 1. Feladat
adatok = []
fbe = open("melyseg.txt")
for i in fbe:
    adatok.append(int(i.strip()))
fbe.close()
print(f"1. feladat\nA fájl adatainak száma: {len(adatok)}\n")

# 2. Feladat
tavolsag = 9  # int(input("2. feladat\nAdjon meg egy távolságértéket! "))
print(f"Ezen a helyen a felszín {adatok[tavolsag - 1]} méter mélyen van\n")

# 3. Feladat
print(f"3. feladat\nAz érintettlen területek aránya {round(adatok.count(0) / len(adatok) * 100, 2)}%\n")

# 4. Feladat
egygodor = []
szaml = 0  # 5. feladathoz
fki = open("godrok.txt", "w")
for i in adatok:
    if i != 0:
        egygodor.append(i)
    elif i == 0 and len(egygodor) > 0:
        print(*egygodor, file=fki)
        egygodor = []
        szaml += 1
fki.close()

# 5. Feladat
print(f"5. feladat\nA gödrök száma: {szaml}")

# 6. Feladat
print("6. feladat")
if adatok[tavolsag] == 0:
    print("Az adott helyen nincs gödör.")

print("a)")
kezdindex = tavolsag
vegindex = tavolsag
while True:
    if adatok[kezdindex - 1] != 0:
        kezdindex -= 1
    if adatok[vegindex + 1] != 0:
        vegindex += 1
    if adatok[vegindex + 1] == 0 and adatok[kezdindex - 1] == 0:
        break
print(f"A gödör kezdete: {kezdindex + 1} méter, a gödör vége: {vegindex + 1} méter.")

print("b)")
godor = adatok[kezdindex:vegindex + 1]
fordult = 0
for i in range(len(godor)):
    if godor[i] <= godor[i + 1]:
        fordult += 1
    elif fordult == 1 and godor[i] <= godor[i + 1]:
        print("Nem mélyül folyamatosan")
        break
    elif fordult > 1:
        print("Nem mélyül folyamatosan")
        break

print(f"c)\nA legnagyobb mélység {max(godor)} méter.")

print(f"d)\nA térfogata {sum(godor) * 10} cm^3.")

print(f"e)\nA víz mennyisége {(sum(godor) - len(godor)) * 10} m^3.")
