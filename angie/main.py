# sister_mary.angie.main.py
# Projeto Jogo Miguel 13/02/2025
from _spy.vitollino.main import Cena, Elemento
from browser import document
CENA0 = "https://i.imgur.com/kJrBXt8.jpeg"
CENA1 = "https://imgur.com/0cqfufR.jpeg"
HEROI0 = "https://i.imgur.com/WQ2l5kM.png"

aqui = Cena(CENA0)
aqui.vai()
coisa = Elemento(HEROI0)
coisa.entra(aqui)
coisax = 0
def anda(evento):
    global coisax, coisa
    event.stopPropagation()
    evento.preventDefault()
    if(evento.keyCode == 37) :
        coisax += 10
        coisa.x = coisax

document.bind("keypress", anda)
