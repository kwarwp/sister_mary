# sister_mary.roxanne.main.py
# Jogo do Gato
from browser import document, html
class Recusos:
    CENA0 = "https://i.imgur.com/kJrBXt8.jpeg"
    HEROI0 = "https://i.imgur.com/WQ2l5kM.png"
    
    
class Cena:
    def __init__(self, recurso_cena, jogo):
        self.cena = html.DIV(Id="_cena")
        self.cena <= html.IMG(src=recurso_cena)
        jogo <= self.cena
        
        
if __name__ == "__main__":
    Cena(Recursos.CENA0, document["pydiv"])