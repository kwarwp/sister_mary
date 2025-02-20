# sister_mary.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
from random import randint
STYLE.update(width=1250, height="650px")
FLORA = "https://i.imgur.com/n3GnL9B.png"
MATA0 = "https://i.imgur.com/TT2FKyu.jpeg"
TORA = "https://imgur.com/0jSB27g.png"
FX, FY = 5, 4
TREES = 300
LAYERS = 8

class Lax:
    def __init__(self):
        self.c = Cena(MATA0)
        self.c.elt.style.overflow="hidden"
        self.c.vai()
        self.layers = [Elemento(w=2000, h=700, cena=self.c) for _ in range(LAYERS)] #[list()]*LAYERS
        self.scenery()
        
    def scenery(self, trees=16):
        fls = front_layer_size = 1600
        flx = 600 - fls//2
        def off_lay(layer, off):
            scale = 1.0+ off /5.0
            layer.y = 150 + 100*off -300
            layer.x = layer.x + 65*off
            layer.elt.style.scale = scale
        def sl(layer):
            # return 8//(layer+1)*1200
            off = (LAYERS-layer+1)
            return fls-flx*off -off*layer*trees
        #[lay.elt <= self.sprite(item*(sl(layer)//trees)+randint(0,10)-100, 350-randint(0,15), randint(0,15), layer)
        [lay.elt <= self.sprite(150*item-300, 350, randint(0,15), 1, layer)
        for layer, lay in enumerate(self.layers) for item in range(0, trees)]
        [off_lay(lay, layer) for layer, lay in enumerate(self.layers)]
        
        
    def _scenery_(self, trees=8):
        # tr = [self.sprite(tr*(1200//trees)+randint(0,10)-100, 20*5*layer-randint(0,15), randint(0,20), layer)
        fls = front_layer_size = 1600
        flx = 600 - fls//2
        def sl(layer):
            # return 8//(layer+1)*1200
            off = (LAYERS-layer+1)
            return fls-flx*off -off*layer*trees
        #lay = self.layers[0]
        [lay.elt <= self.sprite(item*(sl(layer)//trees)-layer*150, 750, 0, 8)
        for layer, lay in enumerate(self.layers[::-1]) for item in range(0, trees)]
        
    def scenery_(self, trees=8):
        # tr = [self.sprite(tr*(1200//trees)+randint(0,10)-100, 20*5*layer-randint(0,15), randint(0,20), layer)
        fls = front_layer_size = 2000
        flx = 600 - fls//2
        def sl(layer):
            return 8//(LAYERS - layer+1)*1200
        #[lay.elt <= self.sprite(item*(sl(layer)//trees)+randint(0,10)-100, 350-randint(0,15), randint(0,15), layer)
        [lay.elt <= self.sprite(item*(sl(layer)//trees)+randint(0,10)-100, 350-randint(0,14), 0, layer)
        for layer, lay in enumerate(self.layers) for item in range(0, trees)]
        #self.layers = [[self.sprite(tr*(1200//trees)+randint(0,10)-100, 350-randint(0,15), randint(0,20), layer)
        #for tr in range(0, trees)] for layer in range(LAYERS,1,-1)]
        
    def sprite(self, x, y, item, layer, ly):
        """Near layer should be more spaced"""
        item = randint(4,8)
        item = ly+1
        layer_delta_y = 400//LAYERS
        conta_ = FX - 1 if FX > 1 else 1
        lado_ = FY - 1 if FY > 1 else 1
        dw, dh = (100/conta_)*(p % FX), (100/lado_)*(p // FX)
        # dw, dh, size = 100 // (FX-1), 100 // (FY-1), FX*FY
        ox, oy = item // FX, item % FX
        bp = f"{dw:.2f}% {dh:.2f}%"
        size = TREES - layer * 30
        e = Elemento(FLORA, w=size-10, h=size, x=x, y=y-layer*layer_delta_y, cena=self.c)
        #e.o = layer / 10 + 0.2
        e.elt.style.backgroundSize = f"{FX*100}% {FY*100}%"
        e.elt.style.backgroundPosition = bp
        # e.elt.style.backgroundPosition = f"{ox*dw}% {oy*dh}%"
        #e.elt.style.backgroundPosition = f"50% 66%"
        # e.elt.style.backgroundPositionY = f""
        return e.elt
    
        
        
Lax()