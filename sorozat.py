
import random

# Dobások véletlen számsorozatának generálása és kiíratása kötőjelekkel elválasztva
def dobassorozat(dobasok):
    eredmenyek = [random.choice([0, 1]) for _ in range(dobasok)]  # 0: írás, 1: fej
    sorozat_str = "-".join(str(i) for i in eredmenyek[:-1])  # "-" elválasztóval, utolsó utáni érték nélkül
    print(sorozat_str)

    return eredmenyek

# Fejek számának megszámolása a dobások között
def fejek_szama(eredmenyek):
    return eredmenyek.count(1)  # Számolja meg, hány fej (1) van az eredmények között

# Eredmények kiíratása a konzolra
def konzol_kiir(eredmenyek):
    fej_szam = fejek_szama(eredmenyek)
    print(f"A fejek száma: {fej_szam}.")

# Eredmények kiíratása fájlba
def file_kiir(eredmenyek):
    fej_szam = fejek_szama(eredmenyek)
    with open("fejek.txt", "w") as file:
        file.write(f"A fejek száma: {fej_szam}.")

# Dobások számának megadása és műveletek végrehajtása
dobasok = 7  # Például 7 dobás
eredmenyek = dobassorozat(dobasok)
konzol_kiir(eredmenyek)
file_kiir(eredmenyek)
