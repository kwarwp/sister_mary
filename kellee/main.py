# sister_mary.kellee.main.py
from _spy.vitollino.main import Cena,Sala

IMAGEM_NORTE = "https://imgur.com/inUG43J" #CIDADECHARN
IMAGEM_SUL = "https://imgur.com/GnOVugz" #PORTAS
IMAGEM_LESTE = "https://imgur.com/inUG43J"
IMAGEM_OESTE ="https://imgur.com/GnOVugz"

cidadeCharn_norte = Cena(IMAGEM_NORTE)
portas_sul= Cena(IMAGEM_SUL)
cidadeCharn_leste = Cena(IMAGEM_LESTE)
portas_oeste= Cena(IMAGEM_OESTE)


historia=Sala(n=cidadeCharn_norte, s=portas_sul, L=cidadeCharn_leste, O=portas_oeste)

cidadeCharn_norte.vai()
#portas_sul.vai()
#cidadeCharn_leste.vai()
#portas_oeste.vai()

















