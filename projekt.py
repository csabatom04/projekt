
from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=14999, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=29999, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

szalloda = Szalloda(nev="HotelHell")

szalloda.add_szoba(EgyagyasSzoba(szobaszam=11))
szalloda.add_szoba(EgyagyasSzoba(szobaszam=12))
szalloda.add_szoba(KetagyasSzoba(szobaszam=13))

foglalaskezelo = FoglalasKezelo(szalloda)
foglalaskezelo.foglalas(szobaszam=11, datum=datetime(2024, 5, 10))
foglalaskezelo.foglalas(szobaszam=12, datum=datetime(2024, 5, 15))
foglalaskezelo.foglalas(szobaszam=13, datum=datetime(2024, 5, 20))
foglalaskezelo.foglalas(szobaszam=11, datum=datetime(2024, 5, 25))
foglalaskezelo.foglalas(szobaszam=12, datum=datetime(2024, 5, 30))

def hotel():
    while True:
        print(" ~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("| Hotel Hell | We make your dreams come True |")
        print(" ~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("<=============>\n1. Foglalás\n----------\n2. Lemondás\n----------\n3. Foglalások listázása\n----------\n4. Szoba információk\n----------\n5. Kilépés\n<=============>")
        valasztas = input("Válasszon műveletet: ")

        if valasztas == "1":
            print("----------")
            szobaszam = int(input("Adja meg a szoba számát: "))
            print("----------")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            ar = foglalaskezelo.foglalas(szobaszam, datum)
            if ar is not None:
                print("----------")
                print(f"Sikeres foglalás! Ár: {ar}")
            else:
                print("----------")
                print("Nem sikerült foglalni a szobát.")

        elif valasztas == "2":
            print("----------")
            szobaszam = int(input("Adja meg a lemondani kívánt foglalás szobaszámát: "))
            print("----------")
            datum_str = input("Adja meg a lemondani kívánt foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            lemondando_foglalas = None
            for foglalas in foglalaskezelo.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    lemondando_foglalas = foglalas
                    break
            if lemondando_foglalas is not None:
                foglalaskezelo.lemondas(lemondando_foglalas)
                print("----------")
                print("Sikeres lemondás!")
            else:
                print("----------")
                print("Nem található ilyen foglalás.")

        elif valasztas == "3":
            print("----------")
            print("Íme, a foglalásaink:")
            print("----------")
            foglalaskezelo.listaz_foglalasok()

        elif valasztas == "5":
            break

        elif valasztas == "4":
            print("----------")
            print("Egyágyas szobák: 11, 12\n----------\nKétágyas szoba: 13")
            
        else:
            print("----------")
            print("Érvénytelen választás.")

if __name__ == "__main__":
    hotel()