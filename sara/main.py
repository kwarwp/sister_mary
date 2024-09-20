# sister_mary.sara.main.py
""""Experimentando IA.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Miguel Roman <migdukaroma@gmail.com>

Changelog
---------
.. versionadded::    24.09
   |br| Início (20).

|   **Open Source Notification:** This file is part of open source program **Carro IA**
|   **Copyright © 2024  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
import random
from random import choice
# print(choice(range(100)))


class Pista:
    def __init__(self):
        self.pista = [3,4]
        self.largura = 1
        self.inicio = [0, 4]
        self.fim = [3, 0]
        
    def dentro(self, x, y):
        x0, x1 = self.inicio[0] - self.largura,self.inicio[0] + self.pista[0] + self.largura
        x2, x3 = self.fim[0] - self.largura,self.fim[0] +  self.largura 
        
        y0, y1 = self.inicio[1] - self.largura,self.inicio[1] + self.largura
        y2, y3 = self.fim[1] - self.largura,self.fim[1] + self.pista[1] + self.largura 
        # x0, x1, x2, x3, y0, y1, y2, y3 = -1, 4, 2, 4, 3, 5, -1, 5 
        oka = (x0 <= x <= x1) and (y0 <= y <= y1)
        okb = (x2 <= x <= x3) and (y2 <= y <= y3)
        ok = oka or okb
        return ok
        
class Carro:
    def __init__(self):
        self.carro = [1, 1]
        self.velocidade = [1, 0]
        self.posicao = [0, 0]
        self.tempo = 0
        
    def move(self,x,y):
        self.posicao = [x, y]
        
    def anda(self):
        self.tempo += 1
        self.posicao = self.posicao[0]+self.velocidade[0], self.posicao[1]+self.velocidade[1]
        
if __name__ == "__main__":
    pista = Pista()
    carro = Carro()
    carro.move(*pista.inicio)
    print(carro.posicao, pista.dentro(*carro.posicao))
    [carro.anda() for _ in range(3)]
    print(carro.posicao, carro.tempo, pista.dentro(*carro.posicao))
    carro.velocidade = [0, -1]
    [carro.anda() for _ in range(4)]
    print(carro.posicao, carro.tempo, pista.dentro(*carro.posicao))
        