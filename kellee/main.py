# sister_mary.kellee.main.py
from _spy.vitollino.main import Cena,Sala,Texto

IMAGEM_NORTE = "https://i.imgur.com/inUG43J.png" #CIDADECHARN
IMAGEM_SUL = "https://i.imgur.com/GnOVugz.png" #PORTAS
IMAGEM_LESTE = "https://i.imgur.com/inUG43J.png"
IMAGEM_OESTE ="https://i.imgur.com/GnOVugz.png"

cidadeCharn_norte = Cena(IMAGEM_NORTE)
portas_sul= Cena(IMAGEM_SUL)
cidadeCharn_leste = Cena(IMAGEM_LESTE)
portas_oeste= Cena(IMAGEM_OESTE)


historia=Sala(n=cidadeCharn_norte, s=portas_sul, l=cidadeCharn_leste, o=portas_oeste)
TextoIntroducao=Texto(cidadeCharn_norte, """No universo de fantasia das Cróicas Nárnia , Polly Plummer, uma aventureira e curiosa garotinha de 11 anos, fica presa na devastada cidade de Charn.
 Ajude-a a encontrar a chave correta para abrir a porta que a transportará de volta para o jardim da Nárnia, um lugar mágico construído e protegido pelo leão Aslam.""").vai()

cidadeCharn_norte.vai()
#portas_sul.vai()
#cidadeCharn_leste.vai()
#portas_oeste.vai()

















