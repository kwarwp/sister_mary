# sister_mary.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=1250, height="650px")
FLORA = "https://i.imgur.com/n3GnL9B.png"
MATA0 = "https://i.imgur.com/TT2FKyu.jpeg"
FX, FY = 5, 4
TREES = 600

class Lax:
    def __init__(self):
        self.c = Cena(MATA0)
        # self.e = Elemento(FLORA,w=1250,h=1000, cena = c)
        self.c.vai()
        t = self.sprite(0, 0, 0, 0)
        t = self.sprite(300, 0, 6, 0)
        t = self.sprite(600, 0, 12, 0)
        
    def sprite(self, x, y, item, layer):
        dw, dh, size = 100 // (FX-1), 100 // (FY-1), FX*FY
        ox, oy = item // FX, item % FX
        size = TREES - layer * 30
        e = Elemento(FLORA, w=size, h=size, x=x, y=y+layer*15, cena=self.c)
        e.elt.style.backgroundSize = f"{FX*100}% {FY*100}%"
        e.elt.style.backgroundPosition = f"{ox*dw}% {oy*dh}%"
        #e.elt.style.backgroundPosition = f"50% 66%"
        # e.elt.style.backgroundPositionY = f""
        return e
    
        
        
Lax()