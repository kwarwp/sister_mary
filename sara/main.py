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
        
class Carro:
    def __init__(self):
        self.carro = [1, 1]
        self.velocidade = [0, 0]
        self.posicao = [0, 0]
        
    def move(self,x,y):
        self.posicao = [x, y]
        
    def anda(self):
        self.posicao = self.posicao[0]+self.velocidade[0], self.posicao[1]+self.velocidade[1]
        
if __name__ == "__main__":
    carro = Carro()
    print(carro.posicao)
    carro.anda()
    print(carro.posicao)
        