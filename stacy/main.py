# sister_mary.stacy.main.py
# Calculadora

class Calculadora:
    def __init__(self):
        self.ops = dict(a=None, d=None, m=None)
        self.reg = 0
        
    def add(self, op):
        result = self.reg + op
        
    def operate(self):
        self.reg = input("escolha um número:")
        get_ops = input("escolha uma operção (a, d, m):")
        op = input("escolha outro número:")
        if get_ops in self.ops:
            self.ops[get_ops](op)
        else:
            input("operação inválida")
        
Calculadora().add().operate()
        