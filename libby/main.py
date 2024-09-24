# sister_mary.libby.main.py_Raquel Brayner
from _spy.vitollino.main import Cena, Elemento, Texto 

# salvando o link no código primeiro
LinkCidadeCharn = "https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/bf4d9c8d-f5cf-4571-9ac3-b26154c673f6/DallEGeneratedImages/dalle-221735ad-13e5-45a5-ad43-806d169277440251675098881199351800.jpg&dcHint=BrazilSouth&fileToken=1b21d0be-54e6-4bac-8f89-f042cff4cd62"
Pergaminho = "https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/bf4d9c8d-f5cf-4571-9ac3-b26154c673f6/DallEGeneratedImages/dalle-93556656-0c50-40e1-a836-3b76b1deb0d60251675096053234399000.jpg&dcHint=BrazilSouth&fileToken=1b21d0be-54e6-4bac-8f89-f042cff4cd62"


#instruções para a primeira parte da históra
def Historia():
	cenaCharn = Cena(img = "https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/bf4d9c8d-f5cf-4571-9ac3-b26154c673f6/DallEGeneratedImages/dalle-221735ad-13e5-45a5-ad43-806d169277440251675098881199351800.jpg&dcHint=BrazilSouth&fileToken=1b21d0be-54e6-4bac-8f89-f042cff4cd62")
	Pergaminho = Elemento (img = "Pergaminho", style=dict(left=150, width=60, height=200))
	Pergaminho.entra(cenaCharn)    
	cenaCharn.vai()    
    
Historia()