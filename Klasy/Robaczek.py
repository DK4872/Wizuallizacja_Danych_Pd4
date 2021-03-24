class Robaczek:
    xaxis = 0
    yaxis = 0
    krok = 0

    def __init__(self, x=0, y=0, step=1):
        self.xaxis = x
        self.yaxis = y
        self.krok = step

    def idz_w_gore(self, ile):
        self.yaxis += (ile * self.krok)

    def idz_w_dol(self, ile):
        self.yaxis -= (ile * self.krok)

    def idz_w_lewo(self, ile):
        self.xaxis -= (ile * self.krok)

    def idz_w_prawo(self, ile):
        self.xaxis += (ile * self.krok)

    def pokaz_gdzie_jestes(self):
        print("Wspolrzedna x: " + str(self.xaxis) + " Wspolrzedna y: " + str(self.yaxis))
