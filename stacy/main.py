# sister_mary.stacy.main.py
# Calculadora

class Calculadora:
    def __init__(self):
        self.ops = dict(a=self.add, d=self.div, m=self.mul)
        self.reg = 0
        self.options = "a"
        
    def add(self, op):
        return self.reg + op
         
    def div(self, op):
        return self.reg // op
         
    def mul(self, op):
        return self.reg * op
        
    def operate(self):
        self.reg = int(input("escolha um número:"))
        # get_ops = input("escolha uma operção (a, d, m):")
        op = int(input("escolha outro número:"))
        if self.options in self.ops:
            input(f" resultado: {self.ops[self.options](op)}")
        else:
            input("operação inválida")
            
    def run(self):
        self.options = str(input('Escolha uma das seguintes operações (m, a, d):'))
        self.operate()
        
        
# Calculadora().add().operate()

class Calculadora_:
    def __init__(self):
        self.answers = ['m', 'a', 'd']
        self.options = str(input('Escolha uma das seguintes operações (m, a, d):'))
    def run(self):
        while True:
            if self.options in self.answers:
                print('Insiraos dois valores:')
                val1 = int(input('valor 1;'))
                val2 = int(input('valor 2;'))
                if self.options == 'm':
                    print(f"{val1}*{val2}={val1} * {val2}")
                elif self.options == 'a':
                    print(val1, '+', val2, '=', val1 + val2)
                elif self.options == 'd':
                    print(val1, '/', val2, '=', val1 / val2)
        
        
Calculadora().run()
        
        