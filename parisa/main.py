# sister_mary.parisa.main.py
""""Pique de avalição da paralaxe para a plataforma Sucuri.

Classes neste módulo:
    - :py:class:`LAX` Spike to demonstrate a crude paralax mechanism.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    25.02
   |br| Crude scenery creation (18).
   |br| key capture and paralax calculation (20).

|   **Open Source Notification:** This file is part of open source program **Suucurijuba**
|   **Copyright © 2025  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http:#is.gd/3Udt>`_.
|   `Labase <http:#labase.selfip.org/>`_ - `NCE <https:#portal.nce.ufrj.br>`_ - `UFRJ <https:#ufrj.br/>`_.
"""

from _spy.vitollino.main import Cena, Elemento, STYLE
from browser import document
from random import randint
STYLE.update(width=1250, height="650px")
FLORA = "https://i.imgur.com/n3GnL9B.png"
MATA0 = "https://i.imgur.com/TT2FKyu.jpeg"
TORA = "https://imgur.com/0jSB27g.png"
FX, FY = 5, 4
KX, KY = 6, 1
TREES = 300
LAYERS = 8
KIRI ="https://i.imgur.com/gPnv2KM.png"


class Lax:
    def __init__(self):
        self.walk = self.right
        self.spriter = 3
        self.c = Cena(MATA0)
        self.c.elt.style.overflow="hidden"
        self.c.vai()
        self.layers = [Elemento(w=4000, h=700, cena=self.c) for _ in range(LAYERS)] #[list()]*LAYERS
        self.scenery()        
        # document.bind("keydown", self.anda)
        self.k = self.sprite_kiri(600, 450, self.spriter)
        self.k.elt.bind("click", self.right)
        

    def right(self, evento):
        self.spriter = (self.spriter-3 + 1) % 3 + 3
        self.k = self.sprite_kiri(600, 450, self.spriter)
        

    def anda(self, evento):
        global coisax, coisa
        evento.stopPropagation()
        evento.preventDefault()
        if(evento.keyCode == 37):
            self.move()
        elif (evento.keyCode == 39):
            self.move(-40)
            
    def move(self, val=40):
        def mover(lay, val_):
            lay.x = lay.x +val_
        [mover(lay, val* (layer+1)) for layer, lay in enumerate(self.layers)]

    def scenery(self, trees=32):
        def off_lay(layer, off):
            scale = 1.0+ off /5.0
            layer.y = 150 + 100*off -300
            layer.x = layer.x + 65*off
            layer.elt.style.scale = scale
            layer.elt.style.transition = "left 1s"
        [lay.elt <= self.sprite(150*item-3000, 350, randint(0,15), 1, layer)
        for layer, lay in enumerate(self.layers) for item in range(0, trees)]
        [off_lay(lay, layer) for layer, lay in enumerate(self.layers)]
        
        
    def sprite_kiri(self, x, y, item):
        """Near layer should be more spaced"""
        # item = ly+1
        conta_, lado_ = KX - 1 if KX > 1 else 1, KY - 1 if KY > 1 else 1
        dw, dh = (100/conta_)*(item % KX), (100/lado_)*(item // KX)
        bp = f"{dw:.2f}% {dh:.2f}%"
        e = Elemento(KIRI, w=130, h=250, x=x, y=y, cena=self.c)
        e.elt.style.backgroundSize = f"{KX*100}% {KY*100}%"
        e.elt.style.backgroundPosition = bp
        return e.elt
        
    def _scenery_(self, trees=8):
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
        
    def sprite(self, x, y, item, layer, ly, elt=None):
        """Near layer should be more spaced"""
        item = randint(0,14)
        # item = ly+1
        layer_delta_y = 400//LAYERS
        conta_, lado_ = FX - 1 if FX > 1 else 1, FY - 1 if FY > 1 else 1
        dw, dh = (100/conta_)*(item % FX), (100/lado_)*(item // FX)
        bp = f"{dw:.2f}% {dh:.2f}%"
        size = TREES - layer * 30
        e = elt or Elemento(FLORA, w=size-10, h=size, x=x, y=y-layer*layer_delta_y, cena=self.c)
        #e.o = ly / 10 + 0.4
        e.elt.style.backgroundSize = f"{FX*100}% {FY*100}%"
        e.elt.style.backgroundPosition = bp
        return e.elt
    
        
        
Lax()