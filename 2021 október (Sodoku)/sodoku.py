# 1. Feladat
file = "konnyu.txt"  # input("1. feladat\nAdja meg a bemeneti fájl nevét! ")
sor = int(input("Adja meg egy sor számát! ")) - 1
oszlop = int(input("Adja meg egy oszlop számát! ")) - 1


# 2. Feladat
tabla = []
megoldas = []
fbe = open(file)
for i in fbe:
    i = i.strip().split()
    tabla.append([int(x) for x in i if len(i) > 3])
    if len(i) == 3:
        megoldas.append([int(x) for x in i])
tabla = [x for x in tabla if x]
fbe.close()


# 3. Feladat
print(f"3. feladat\nAz adott helyen szereplő szám: {tabla[sor][oszlop]}"
      f"\nA hely a(z) {3 * (sor // 3) + (oszlop // 3) + 1} résztáblázathoz tartozik.")


# 4. Feladat
hiany = 0
for i in tabla:
    hiany += i.count(0)
print(f"4. feladat\nAz üres helyek aránya: {round(hiany / (9*len(tabla)) * 100, 1)}% ")


# 5. Feladat
print("5. Feladat")
for i in megoldas:
    kapcs = False
    print(f"A kiválasztott sor: {i[1]} oszlop: {i[2]} a szám: {i[0]}")

    if tabla[sor][oszlop]:
        print("A helyet már kitöltötték.\n")
    else:
        if megoldas[0] in tabla[sor]:
            print("Az adott sorban már szerepel a szám.\n")
        else:
            for s in range(9):
                if tabla[s][oszlop] == megoldas[0]:
                    kapcs = True
                    break
            if kapcs:
                print("Az adott oszlopban már szerepel a szám.\n")
            else:
                for s in range(3 * (sor // 3), 3 * (sor // 3) + 3):
                    for o in range(3 * (oszlop // 3), 3 * (oszlop // 3) + 3):
                        if tabla[s][o] == megoldas[0]:
                            kapcs = True
                if kapcs:
                    print("A résztáblázatban már szerepel a szám.\n")
                else:
                    print("A lépés megtehető.\n")