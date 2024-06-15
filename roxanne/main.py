# sister_mary.roxanne.main.py
# Jogo do Gato
from browser import document, html
class Recursos:
    CENA0 = "https://i.imgur.com/kJrBXt8.jpeg"
    HEROI0 = "https://i.imgur.com/WQ2l5kM.png"
    
    
class Cena:
    def __init__(self, recurso_cena, jogo):
        self.cena = html.DIV(Id="_cena_")
        self.cena <= html.IMG(src=recurso_cena)
        jogo <= self.cena
    
    
class Heroi:
    def __init__(self, recurso_heroi, jogo):
        self.heroi = html.DIV(Id="_heroi_", style=dict(position="absolute", top="400px"))
        self.heroi <= html.IMG(src=recurso_heroi)
        jogo <= self.heroi
        
        
if __name__ == "__main__":
    Cena(Recursos.CENA0, document["pydiv"])
    Heroi(Recursos.HEROI0, document["pydiv"])