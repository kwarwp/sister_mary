# sister_mary.kellee.main.py
from _spy.vitollino.main import Cena,Sala, STYLE

STYLE['width'] = 900
STYLE['height'] = "600px"

IMAGEM_NORTE = "https://imgur.com/inUG43J" #CIDADECHARN
IMAGEM_SUL = "https://imgur.com/GnOVugz" #PORTAS
#IMAGEM_LESTE =
#IMAGEM_OESTE =

cidadeCharn_norte = Cena(IMAGEM_NORTE)
portas_sul= Cena(IMAGEM_SUL)

historia=Sala(n=cidadeCharn_norte, s=IMAGEM_SUL)

cidadeCharn_norte.vai()
portas_sul.vai()

















