# sister_mary.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import randint
STYLE.update(width=1250, height="650px")
FLORA = "https://i.imgur.com/n3GnL9B.png"
MATA0 = "https://i.imgur.com/TT2FKyu.jpeg"
FX, FY = 5, 4
TREES = 500
LAYERS = 8

class Lax:
    def __init__(self):
        self.c = Cena(MATA0)
        self.c.elt.style.overflow="hidden"
        # self.e = Elemento(FLORA,w=1250,h=1000, cena = c)
        self.c.vai()
        self.layers = [Elemento(cena=self.c) for _ in range(0, LAYERS)] #[list()]*LAYERS
        self.scenery()
        #return
        '''
        t = self.sprite(0, 300, 0, 1)
        t = self.sprite(300, 300, 6, 4)
        t = self.sprite(600, 300, 12, 8)
        '''
        
    def scenery(self, trees=8):
        # tr = [self.sprite(tr*(1200//trees)+randint(0,10)-100, 20*5*layer-randint(0,15), randint(0,20), layer)
        [lay.elt <= self.sprite(item*(1200//trees)+randint(0,10)-100, 350-randint(0,15), randint(0,20), layer)
        for layer, lay in enumerate(self.layers) for item in range(0, trees)]
        #self.layers = [[self.sprite(tr*(1200//trees)+randint(0,10)-100, 350-randint(0,15), randint(0,20), layer)
        #for tr in range(0, trees)] for layer in range(LAYERS,1,-1)]
        
    def sprite(self, x, y, item, layer):
        dw, dh, size = 100 // (FX-1), 100 // (FY-1), FX*FY
        ox, oy = item // FX, item % FX
        size = TREES - layer * 30
        e = Elemento(FLORA, w=size, h=size, x=x, y=y-layer*30, cena=self.c)
        #e.o = layer / 10 + 0.2
        e.elt.style.backgroundSize = f"{FX*100}% {FY*100}%"
        e.elt.style.backgroundPosition = f"{ox*dw}% {oy*dh}%"
        #e.elt.style.backgroundPosition = f"50% 66%"
        # e.elt.style.backgroundPositionY = f""
        return e
    
        
        
Lax()