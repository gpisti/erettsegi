def mpbe(o, p, mp):
    m = o * 3600 + p * 60 + mp
    return m

def vissza(mp):
    ora = mp // 3600
    mp = mp % 3600
    perc = mp // 60
    mp = mp % 60
    ido = [ora, perc, mp]
    return ido

# 2. Feladat
fv = open('hivas.txt')
adatok = []
for sor in fv:
    sor = sor.strip().split()
    sor2 = []
    for elem in sor:
        sor2.append(int(elem))
    k = mpbe(sor2[0], sor2[1], sor2[2])
    v = mpbe(sor2[3], sor2[4], sor2[5])
    ido_adatok = []
    ido_adatok.append(k)
    ido_adatok.append(v)
    adatok.append(ido_adatok)
fv.close()

# 3. Feladat
print('3.feladat - óránkénti hívások száma')
ora = [0] * 24
for elem in adatok:
    index = elem[0] // 3600
    ora[index] += 1

for óra in range(0, 24):
    if ora[óra] != 0:
        print('{} óra {} hívás'.format(óra, ora[óra]))

# 4. Feladat
print('4. feladat')
hívás_hosszak = []
for elem in adatok:
    hívás_hosszak.append(elem[1] - elem[0])  # vége-kezdés mp-ben
leghosszabb = max(hívás_hosszak)
sorszam = hívás_hosszak.index(leghosszabb) + 1  # leghosszabb sorszáma
print('A leghosszabb ideig vonalban levo hivo %d. sorban szerepel, a hivas hossza: %d masodperc.' % (
sorszam, leghosszabb))

# 5. Feladat
print('5. feladat')
print('Kérek egy időpontot: ')
ora = int(input('Óra: '))
perc = int(input('Perc: '))
mp = int(input('Másodperc: '))
keres = mpbe(ora, perc, mp)
varakozok = 0
beszelo = 0
for elem in adatok:
    if keres >= elem[0] and keres <= elem[1]:
        if beszelo == 0:
            beszelo = adatok.index(elem) + 1
        varakozok += 1
if beszelo != 0:  # van találat
    print('A várakozók száma: {}, a beszélő a(z) {}. hivo.'.format(varakozok - 1, beszelo))
else:
    print('Nem volt beszélő.')

# 6. Feladat
print('6. feladat')
utolso = 0
ora12 = mpbe(12, 0, 0)
for i in range(len(adatok)):
    if adatok[i][0] < ora12 and adatok[i][1] > adatok[utolso][1]:
        elozo = utolso
        utolso = i

varakozas = adatok[elozo][1] - adatok[utolso][0]
print('Az utolsó telefonáló adatai a(z) {}. sorban vannak, {} masodpercig várt.'.format(utolso + 1, varakozas))

# 7. Feladat
print('7. feladat - sikeres.txt fájl írása')
def kiírás(index, előző):
    if adatok[előző][1] < ora8:
        kezdőidőpont_beszélő = vissza(ora8)
    else:
        kezdőidőpont_beszélő = vissza(adatok[előző][1])

    végeidőpont_beszélő = vissza(adatok[index][1])
    fájl_sor = ''
    fájl_sor = str(index + 1) + ' '
    for elem in kezdőidőpont_beszélő:
        fájl_sor += (str(elem) + ' ')
    for elem in végeidőpont_beszélő:
        fájl_sor += (str(elem) + ' ')
    fájl_sor += '\n'
    return fájl_sor
fv = open('sikeres.txt', 'w')
ora8 = mpbe(8, 0, 0)
elozo = 0
beszelok = []
for i in range(1, len(adatok)):
    if adatok[i][0] < ora12 and adatok[i][1] > ora8 and adatok[i][1] > adatok[elozo][1]:
        fv.write(kiírás(i, elozo))

        beszelok.append(i)
        elozo = i
fv.close()