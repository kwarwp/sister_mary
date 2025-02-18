# sister_mary.parisa.main.py
from _spy.vitollino.main import Cena, Elemento, STYLE
STYLE.update(width=1200, height="650px")
FLORA = "https://i.imgur.com/ujeUjZj.png"
MATA0 = "https://i.imgur.com/TT2FKyu.jpeg"
c = Cena(MATA0)
e = Elemento(FLORA, cena = c)
c.vai()