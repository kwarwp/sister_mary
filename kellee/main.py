# sister_mary.kellee.main.py
from _spy.vitollino.main import Cena,Sala,Texto,Elemento,STYLE

STYLE['width'] = 900
STYLE['height'] = "600px"

ELementoPolly="https://i.imgur.com/ON2IIrs.png"


IMAGEM_NORTE = "https://i.imgur.com/inUG43J.png" #CIDADECHARN
IMAGEM_LESTE ="https://i.imgur.com/BZq67xa.png"
IMAGEM_SUL = "https://i.imgur.com/BZq67xa.png" #chamada para abrir as portas 
IMAGEM_OESTE ="https://i.imgur.com/rwi0tql.png" #cadeira


cidadeCharn_norte = Cena(IMAGEM_NORTE)
chamada_sul= Cena(IMAGEM_SUL)
cidadeCharn_leste = Cena(IMAGEM_LESTE)
portas_oeste= Cena(IMAGEM_OESTE)
#Polly = Elemento(ELementoPolly,style=dict(height=30,width=150, left=600, top=20))
Polly = Elemento(ELementoPolly,h=250,w=200, x=100, y=300)

def segundaParte():
	Polly.entra(chamada_sul)
	TextoPortas=Texto(chamada_sul, """Rápido! Só temos 3 tentativas!""")
	TextoPortas.vai()
	chamada_sul.vai()
	

historia=Sala(n=cidadeCharn_norte, l=chamada_sul, s=cidadeCharn_leste, o=portas_oeste)
TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""", foi=segundaParte).vai()







#TextoPortas=Texto(portas_sul, """Fala polly: Rápido! Só temos 3 tentativas!""")

cidadeCharn_norte.vai()
#portas_sul.vai()
#cidadeCharn_leste.vai()
#portas_oeste.vai()

















