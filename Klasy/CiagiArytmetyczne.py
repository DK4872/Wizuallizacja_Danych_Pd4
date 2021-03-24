class CiagiArytmetyczne:
    a1 = 0
    roznica = 0
    ile = 0
    wyrazyCiagu = [a1]

    def wyswietlE(self):
        print(self.wyrazyCiagu)

    def pobierzE(self, *n):
        pobraneE = []
        for x in n:
            pobraneE.append(self.wyrazyCiagu[x - 1])
        print(pobraneE)

    def pobierzP(self, a1, roznica, ile):
        self.a1 = a1
        self.roznica = roznica
        self.ile = ile

    def sumaE(self):

        suma = 0
        for x in self.wyrazyCiagu:
            suma += x
        print(suma)

    def policzE(self):
        if self.roznica != 0:
            a1 = self.a1
            for x in range(self.ile):
                an = a1 + self.roznica
                self.wyrazyCiagu.append(an)
                a1 = an
