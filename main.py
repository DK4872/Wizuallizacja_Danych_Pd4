from Klasy import *

print("Zadanie 1")
lista = [0 + x for x in range(1, 31, 1)]
lista2 = [str(x * 2) for x in lista]
plik = open("liczy2.txt", "w")
plik.writelines(lista2)
print("Zadanie 2")
plik = open("liczy2.txt", "r")
zawartosc = plik.readlines()
print(zawartosc)
print("Zadanie 3")
with open("text.txt", "w") as plik:
    for newLine in range(3):
        plik.write("Trzy zdania.\n")
with open("text.txt", "r") as plik:
    for line in plik:
        print(line, end="")
print("Zadanie 4")
produkt = NaZakupy.NaZakupy("Cebula", 4, "Kilogramy", 0.50)
produkt.wyswietl_produkt()
produkt.ilosc_produkt()
print(produkt.cena_produkt())
print("Zadanie 5")
ciag = CiagiArytmetyczne.CiagiArytmetyczne()
ciag.pobierzP(4, 8, 12)
ciag.policzE()
ciag.pobierzE(2, 6, 10)
ciag.sumaE()
ciag.wyswietlE()
print("Zadanie 6")
robaczek = Robaczek.Robaczek()
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_gore(1)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_dol(5)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_lewo(2)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(4)
robaczek.pokaz_gdzie_jestes()
