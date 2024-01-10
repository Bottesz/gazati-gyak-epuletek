class Epulet:
    def __init__(self, nev, varos, orszag, magassag, emeletek, ev):
        self.nev = nev
        self.varos = varos
        self.orszag = orszag
        self.magassag = magassag
        self.emeletek = emeletek
        self.ev = ev

def adatok_beolvasasa(file_nev):
    epuletek = []
    with open(file_nev, "r") as file:
        fejlec = file.readline().strip().split("$")
        for line in file:
            data = line.strip().split("$")
            epulet = Epulet(data[0], data[1], data[2], int(data[3]), int(data[4]), int(data[5]))
            epuletek.append(epulet)
    return epuletek

def epuletek_szama(epuletek):
    return len(epuletek)

def nagyobb_magassagu_epuletek(epuletek, lab_to_meter):
    return sum(epulet.magassag > 555 / lab_to_meter for epulet in epuletek)

def legoregebb_epulet_orszaga(epuletek):
    legoregebb = min(epuletek, key=lambda x: x.ev)
    return legoregebb.orszag

from epulet_kezeles import *

# A) Adatok beolvasása
epuletek = adatok_beolvasasa("epulet.txt")

# B) Épületek száma kiírása
print(f"Az épületek száma: {epuletek_szama(epuletek)}")

# C) 555 lábnál magasabb épületek száma
lab_to_meter = 3.280839895  # 1 méter = 3.280839895 láb
magas_epuletek = nagyobb_magassagu_epuletek(epuletek, lab_to_meter)
print(f"Az 555 lábnál magasabb épületek száma: {magas_epuletek}")

# D) Legöregebb épület országa kiírása
legoregebb_orszag = legoregebb_epulet_orszaga(epuletek)
print(f"A legöregebb épület országa: {legoregebb_orszag}")
