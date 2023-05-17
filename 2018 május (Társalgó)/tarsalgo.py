# 1. Feladat
adatok = []
fbe = open("ajto.txt")
for sor in fbe:
    sor = sor.strip().split()
    adatok.append([int(sor[0]), int(sor[1]), int(sor[2]), sor[3]])
fbe.close()

# 2. Feladat
elso = [x[2] for x in adatok if x[-1] == "be"]
utolso = [x[2] for x in adatok if x[-1] == "ki"]
print(f"2. feladat\nAz első belépő: {elso[0]}\nAz utolsó kilépő: {utolso[-1]}\n")

# 3. Feladat
athaladasok = {}
fki = open("athaladas.txt", "w")
for i in adatok:
    if i[2] in athaladasok:
        athaladasok[i[2]] += 1
    if i[2] not in athaladasok:
        athaladasok[i[2]] = 1
for k, v in sorted(athaladasok.items()):
    print(k, v, file=fki)
fki.close()

# 4. Feladat
bentvan = []
for i in adatok:
    if i[-1] == "be":
        bentvan.append(i[2])
    if i[-1] == "ki":
        try:
            bentvan.remove(i[2])
        except ValueError:
            pass
print("4. feladat\nA végén a társalgóban voltak:", *bentvan)

# 5. Feladat
maxkeres = {}
for i in adatok:
    if f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}" in maxkeres:
        if i[-1] == "be":
            maxkeres[f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}"] += 1
        if i[-1] == "ki":
            maxkeres[f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}"] -= 1
    if f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}" not in maxkeres:
        if i[-1] == "be":
            maxkeres[f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}"] = 1
        if i[-1] == "ki":
            maxkeres[f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}"] = 0
for k, v in maxkeres.items():
    if v == max(maxkeres.values()):
        print(f"\n5. feladat\nPéldául {k}-kor voltak a legtöbben a társalgóban.\n")
        break

# 6. Feladat
azonosito = int(input("6. feladat\nAdja meg egy személy azonosítóját! "))

# 7. Feladat
be, ki = 0, 0
for i in adatok:
    if i[2] == azonosito and i[-1] == "be":
        be += 1  # 8. feladathoz
        print(f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}-", end="")
    if i[2] == azonosito and i[-1] == "ki":
        ki += 1  # 8. feladathoz
        print(f"{str(i[0]).zfill(2)}:{str(i[1]).zfill(2)}")
print()

# 8. Feladat
szaml, ora, perc = 0, 0, 0
for i in adatok:
    if i[2] == azonosito and i[-1] == "be":
        ora, perc = i[0], i[1]
    if i[2] == azonosito and i[-1] == "ki":
        if i[0] == ora:
            szaml += i[1] - perc
        else:
            szaml += (60 - perc) + i[1]
if abs(ki - be) > 0:
    szaml += 60 - perc
print(f"8. feladat\n"
      f"A(z) {azonosito}. személy összesen {szaml} percet volt bent, a megfigyelés végén a társalgóban volt.")
