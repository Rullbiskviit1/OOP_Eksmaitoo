import math

# Klass tehete teostamiseks
class Cal:
    def __init__(self, a, b):
        # Konstruktor määrab kaks arvu objekti atribuutideks
        self.a = a
        self.b = b

    def liitmine(self):
        return self.a + self.b

    def lahutamine(self):
        return self.a - self.b

    def korrutamine(self):
        return self.a * self.b

    # Jagamine, kontrollib nulliga jagamist
    def jagamine(self):
        if self.b == 0:
            return "Nulliga jagada ei saa"
        return self.a / self.b

    # Jäägi leidmine, kontrollib nulliga jagamist
    def jaak(self):
        if self.b == 0:
            return "Nulliga ei saa jääki leida"
        return self.a % self.b

    # Ruutjuure leidmine, kontrollib negatiivseid arve
    def ruutjuur(self):
        if self.a < 0:
            return "Negatiivsel arvul pole reaalarvulist ruutjuurt"
        return math.sqrt(self.a)


# Tehte valik
def menu():
    print(
        "\nVali tehe:"
        "\n1. Liitmine"
        "\n2. Lahutamine"
        "\n3. Korrutamine"
        "\n4. Jagamine"
        "\n5. Jäägi leidmine"
        "\n6. Ruutjuure leidmine"
        "\n0. Välju"
    )

# Küsib arve
def uus_arvud():
    a = float(input("Sisesta esimene number: "))
    b = float(input("Sisesta teine number: "))
    return a, b


# Esimeste arvude sisestamine
a, b = uus_arvud()

# Peamine tsükkel, mis jätkub kuni kasutaja otsustab väljumise
while True:
    kalk = Cal(a, b)  # Loob kalkulaaori
    menu()  # Kuvab menüü
    valik = int(input("Sisesta valik: "))  # Kasutaja valik

    # Tehe vastavalt kasutaja valikule
    if valik == 1:
        vastus = kalk.liitmine()
    elif valik == 2:
        vastus = kalk.lahutamine()
    elif valik == 3:
        vastus = kalk.korrutamine()
    elif valik == 4:
        vastus = kalk.jagamine()
    elif valik == 5:
        vastus = kalk.jaak()
    elif valik == 6:
        vastus = kalk.ruutjuur()
    elif valik == 0:
        print("Head aega!")
        break  # Tsüklist lõpetamine
    else:
        print("Vale valik, proovi uuesti")
        continue  # Tagasi menüüsse, kui vale valik

    print("Vastus:", vastus)

    # Kas jätkata eelneva vastusega või alustada uut tehet
    jatkata = input("Kas soovite jätkata selle numbriga? (jah/ei): ").lower() # .lower() teeb kindlaks, et kalkulaator toimiks ka siis, kui vastuses on suured tähed
    if jatkata == "jah":
        a = vastus  # Eelmine vastus on nüüd esimene arv
        b = float(input("Sisesta uus teine number: "))  # Uus teine arv, millega koostada tehe eelmise vastusega
        continue
    else:
        # Kas alustada täiesti uut tehet või väljuda kalkulaatorist
        uus_valik = input("Kas alustada uut tehet või väljuda? (uus/välju): ").lower()
        if uus_valik == "uus":
            a, b = uus_arvud()  # Sisestab uued arvud
            continue
        else:
            print("Head aega!")
            break  # Tsükli lõpetamine
