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
IMAGEM_OESTE ="https://i.imgur.com/vmgmNvo.png" #AINDA EM TESTE ---- 


cidadeCharn_norte = Cena(IMAGEM_NORTE)
segundaCena_leste = Cena(IMAGEM_LESTE)
terceiraCena_sul= Cena(IMAGEM_SUL)
quartaCena_oeste= Cena(IMAGEM_OESTE)

Polly = Elemento(ELementoPolly,h=300,w=350, x=500, y=300)

#chaves1= Elemento(ElementoChave1,h=100,w=200, x=50, y=500)
#chaves2= Elemento(ElementoChave2,h=100,w=200, x=250, y=500)
#chaves3= Elemento(ElementoChave3,h=120,w=200, x=450, y=500)
#chaves4= Elemento(ElementoChave4,h=100,w=200, x=700, y=500)
#chaves.elt.style={'background-size':"400% 100%"} ----teste hacking


def terceiraParte(*_): 
    terceiraCena_sul.vai()
    return
    chaves1.entra(terceiraCena_sul)
    chaves2.entra(terceiraCena_sul)
    chaves3.entra(terceiraCena_sul)
    chaves4.entra(terceiraCena_sul)
    
class chave():
    def __init__(self,imagem,x,y,cena):
        self.imagem=imagem
        self.x = x
        self.y = y
        self.cena=cena
        self.elemento=chaves1= Elemento(imagem,h=100,w=200, x=x, y=y, cena=cena, vai=self.usa)
    
    def usa(self,*_):
        Texto(self.cena,"Parabéns!Voce voltou pra nárnia!").vai()  
        
chaves1=chave(ElementoChave1,x=50, y=500,cena=terceiraCena_sul)

def segundaParte(*_):
	Polly.entra(segundaCena_leste)
	TextoPortas=Texto(segundaCena_leste, """Rápido! Só temos 3 tentativas!""", foi=terceiraParte) #link para chamar terceira cena
	TextoPortas.vai()
	segundaCena_leste.vai()


historia=Sala(n=cidadeCharn_norte, l=segundaCena_leste, s=terceiraCena_sul, o=quartaCena_oeste)
TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""", foi=segundaParte).vai()

cidadeCharn_norte.vai()
#cidadeCharn_leste.vai()
#portas_sul.vai()
#portas_oeste.vai()


















