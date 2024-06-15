# sister_mary.roxanne.main.py
# Jogo do Gato
from browser import document, html
class Recursos:
    CENA0 = "https://i.imgur.com/kJrBXt8.jpeg"
    CENA1 = "https://imgur.com/0cqfufR.jpeg"
    HEROI0 = "https://i.imgur.com/WQ2l5kM.png"
    
    
class Cena:
    def __init__(self, recurso_cena, jogo):
        self.cena = html.DIV(Id="_cena_", style={
        "background-image":recurso_cena, "width":"1200px", "height":"700px", "overflow":"hidden"})
        #self.cena <= html.IMG(src=recurso_cena, style=dict(
        #position="absolute", width="1200px", height="700px", clip="rect(0, 600px, 800px, 0px)"))
        self.legenda = html.H1("O jogo do Gato", Id="_legenda_", style=dict(
        position="absolute", left=f"110px", top="0px", color="white"))
        self.cena <= self.legenda
        jogo.jogo <= self.cena
        
    def legendar(self, texto):
        self.legenda.innerHTML = texto
        
    
    
class Heroi:
    def __init__(self, recurso_heroi, jogo):
        self.x = 0
        self.jogo = jogo
        self.heroi = html.DIV(Id="_heroi_", style=dict(
        position="absolute", left=f"{self.x}px", top="400px", transform="scaleX(-1)"))
        self.heroi <= html.IMG(src=recurso_heroi)
        self.heroi.bind("click", self.anda)
        jogo.jogo <= self.heroi
        
    def anda(self, ev=0):
        self.x += 100
        self.heroi.style.left = f"{self.x}px"
        self.jogo.cena.legendar(f"O gato andou para {self.x}")
    
    
class Jogo:
    def __init__(self):
        self.jogo = document["pydiv"]
        self.jogo.html = ""
        self.cena = Cena(Recursos.CENA1, self)
        Heroi(Recursos.HEROI0, self)        
        
if __name__ == "__main__":
    Jogo()