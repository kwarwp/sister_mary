# sister_mary.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=1250, height="650px")
FLORA = "https://i.imgur.com/n3GnL9B.png"
MATA0 = "https://i.imgur.com/TT2FKyu.jpeg"
FX, FY = 5, 4

class Lax:
    def __init__(self):
        self.c = Cena(MATA0)
        # self.e = Elemento(FLORA,w=1250,h=1000, cena = c)
        self.c.vai()
        t = self.sprite(0, 0, 0, 0)
        
    def sprite(self, x, y, item, layer):
        dw, dh, size = 100 // FX, 100 // FY, FX*FY
        ox, oy = item // FX, item % FX
        return Elemento(FLORA, w=300, h=300, x=x, y=y, tipo="20% 25%", cena=self.c)
    
        
        
Lax()