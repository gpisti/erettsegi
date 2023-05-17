# 1. Feladat
adatok = []
fbe = open("veetel.txt")
for i in fbe:
    i = i.strip().split()
    if len(i) != 2:
        adatok.append([list(map(int, elozo)), " ".join(i)])
    elozo = i
fbe.close()

# 2. Feladat
print(f"2. feladat:\nAz első üzenet rögzítője: {adatok[0][0][1]}\nAz utolsó üzenet rögzítője: {adatok[-1][0][1]}\n")

# 3. Feladat
print("3. feladat")
for i in adatok:
    if "farkas" in i[1]:
        print(f"{i[0][0]}. nap: {i[0][1]}. rádióamatőr")
print()

# 4. Feladat
print("4. feladat:")
statisztika = dict({x: 0 for x in range(1, 12)})
for i in adatok:
    if i[0][0] in statisztika:
        statisztika[i[0][0]] += 1
for k, v in statisztika.items():
    print(f"{k}. nap: {v} rádióamatőr")

# 5. Feladat
fki = open("aadas.txt", "w")

elozo = adatok[0][1]
megfejtes = ""
for i in adatok:
    for index, j in enumerate(elozo):
        if i[index] == "#" and j != "#":
            adatok[adatok.index(i)][1].replace(i[index], j)
    print(megfejtes)




fki.close()
