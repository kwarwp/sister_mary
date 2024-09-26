# sister_mary.libby.main.py_Raquel Brayner
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE

STYLE['width'] = 900
STYLE['height'] = "600px"

# salvando o link no código primeiro
LinkCidadeCharn = "https://imgur.com/inUG43J"
LinkPortas = "https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/bf4d9c8d-f5cf-4571-9ac3-b26154c673f6/DallEGeneratedImages/dalle-7ccf45fd-d91c-45e0-a5a9-6fd1c7eefcf10251675091894855557900.jpg&dcHint=BrazilSouth&fileToken=1b21d0be-54e6-4bac-8f89-f042cff4cd62"

#instruções para a primeira parte da históra
def HistoriaIntroducao():
	cenaCharn = Cena(img = LinkCidadeCharn)
	textoCharn = Texto(cenaCharn, "No universo de fantasia das Crónicas Nárnia , Polly Plummer, uma aventureira e curiosa garotinha de 11 anos, fica presa na devastada cidade de Charn.Ajude-a a encontrar a chave correta para abrir a porta que a transportará de volta para o jardim da Nárnia, um lugar mágico construído e protegido pelo leão Aslam")
	textoCharn.vai()
	cenaCharn.vai() 
	HistoriaPortas.vai()
HistoriaIntroducao()


def HistoriaPortas():
	cenaPortas = Cena(img= "https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/bf4d9c8d-f5cf-4571-9ac3-b26154c673f6/DallEGeneratedImages/dalle-7ccf45fd-d91c-45e0-a5a9-6fd1c7eefcf10251675091894855557900.jpg&dcHint=BrazilSouth&fileToken=1b21d0be-54e6-4bac-8f89-f042cff4cd62")
	textoPortas = Texto(cenaPortas, "Ajude Polly encontrar a chave correta para sair da cidade devastada Chan e escapar da feiticeira. ")
	textoPortas.vai()
	cenaPortas.vai()

HistoriaPortas()



