# sister_mary.kellee.main.py
from _spy.vitollino.main import Cena,Sala,Texto,Elemento,STYLE

STYLE['width'] = 900
STYLE['height'] = "600px"

ELementoPolly="https://i.imgur.com/ON2IIrs.png"
ElementoChave1="https://i.imgur.com/PymQkYk.png"
ElementoChave2="https://i.imgur.com/uOsjJyl.png"
ElementoChave3="https://i.imgur.com/pSEWTrr.png"
ElementoChave4="https://i.imgur.com/LoLCGBa.png"


IMAGEM_NORTE = "https://i.imgur.com/inUG43J.png" #Introdução|CIDADECHARN
IMAGEM_LESTE ="https://i.imgur.com/BZq67xa.png"#chamada para abrir as portas
IMAGEM_SUL = "https://i.imgur.com/V3o4Xsg.png" #portas|Chaves
IMAGEM_OESTE ="https://i.imgur.com/rwi0tql.png" #teste


cidadeCharn_norte = Cena(IMAGEM_NORTE)
segundaCena_leste = Cena(IMAGEM_LESTE)
terceiraCena_sul= Cena(IMAGEM_SUL)
quartaCena_oeste= Cena(IMAGEM_OESTE)

Polly = Elemento(ELementoPolly,h=300,w=350, x=50, y=300)

chaves1= Elemento(ElementoChave1,h=100,w=200, x=50, y=500)
chaves2= Elemento(ElementoChave2,h=100,w=200, x=250, y=500)
chaves3= Elemento(ElementoChave3,h=120,w=200, x=450, y=500)
chaves4= Elemento(ElementoChave4,h=250,w=200, x=700, y=100)
#chaves.elt.style={'background-size':"400% 100%"} ----teste hacking


def terceiraParte(*_):
	terceiraCena_sul.vai()
	chaves1.entra(terceiraCena_sul)
	chaves2.entra(terceiraCena_sul)
	chaves3.entra(terceiraCena_sul)
	chaves4.entra(terceiraCena_sul)


def segundaParte(*_):
	Polly.entra(segundaCena_leste)
	TextoPortas=Texto(segundaCena_leste, """Rápido! Só temos 3 tentativas!""", foi=terceiraParte)
	TextoPortas.vai()
	segundaCena_leste.vai()


historia=Sala(n=cidadeCharn_norte, l=segundaCena_leste, s=terceiraCena_sul, o=quartaCena_oeste)
TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""", foi=segundaParte).vai()







#TextoPortas=Texto(portas_sul, """Fala polly: Rápido! Só temos 3 tentativas!""")

cidadeCharn_norte.vai()
#portas_sul.vai()
#cidadeCharn_leste.vai()
#portas_oeste.vai()

















