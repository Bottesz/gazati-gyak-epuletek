# Adatok bekérése a felhasználótól
def adatbekeres():
    jatekos_neve = input("Kérem, adja meg a játékos nevét: ")
    jatekos_szerepkore = input("Kérem, adja meg a játékos szerepkörét (varázsló/harcos): ")

# Üdvözlő üzenet megjelenítése a megadott szerepkör alapján
def uzenet():
    if jatekos_szerepkore.lower() == "varázsló":
        print(f"Üdvözlünk {jatekos_neve}, 2 életed van!")
    elif jatekos_szerepkore.lower() == "harcos":
        print(f"Üdvözlünk {jatekos_neve}, 10 életereje van!")
    else:
        print(f"Üdvözlünk {jatekos_neve}, 8 életereje van.")
