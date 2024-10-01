# sister_mary.kellee.main.py
from _spy.vitollino.main import Cena,Sala,Texto,Elemento,STYLE

STYLE['width'] = 900
STYLE['height'] = "600px"



IMAGEM_NORTE = "https://i.imgur.com/inUG43J.png" #CIDADECHARN
IMAGEM_SUL = "https://i.imgur.com/1925t3p.png" #ceu
IMAGEM_LESTE = "https://i.imgur.com/QczYuZh.png" #mato
IMAGEM_OESTE ="https://i.imgur.com/rwi0tql.png" #cadeira


cidadeCharn_norte = Cena(IMAGEM_NORTE)
portas_sul= Cena(IMAGEM_SUL)
cidadeCharn_leste = Cena(IMAGEM_LESTE)
portas_oeste= Cena(IMAGEM_OESTE)

def primeiraParte():
	#portas_sul=Cena(img=IMAGEM_SUL) 
	TextoPortas=Texto(portas_sul, """Rápido! Só temos 3 tentativas!""")
	TextoPortas.vai()
	portas_sul.vai()
	

historia=Sala(n=cidadeCharn_norte, s=portas_sul, l=cidadeCharn_leste, o=portas_oeste)
TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""", foi=primeiraParte).vai()







#TextoPortas=Texto(portas_sul, """Fala polly: Rápido! Só temos 3 tentativas!""")

cidadeCharn_norte.vai()
#portas_sul.vai()
#cidadeCharn_leste.vai()
#portas_oeste.vai()

















