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
        self.legenda = html.H1("O jogo do Gato", Id="_legenda_", style=dict(
        position="absolute", left=f"110px", top="0px"))
        self.cena <= self.legenda
        jogo <= self.cena
    
    
class Heroi:
    def __init__(self, recurso_heroi, jogo):
        self.x = 0
        self.heroi = html.DIV(Id="_heroi_", style=dict(
        position="absolute", left=f"{self.x}px", top="400px", transform="scaleX(-1)"))
        self.heroi <= html.IMG(src=recurso_heroi)
        self.heroi.bind("click", self.anda)
        jogo <= self.heroi
        
    def anda(self, ev=0):
        self.x += 100
        self.heroi.style.left = f"{self.x}px"
    
    
class Jogo:
    def __init__(self):
        self.jogo = document["pydiv"]
        self.jogo.html = ""
        Cena(Recursos.CENA0, self.jogo)
        Heroi(Recursos.HEROI0, self.jogo)        
        
if __name__ == "__main__":
    Jogo()