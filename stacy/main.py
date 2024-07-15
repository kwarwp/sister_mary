# sister_mary.stacy.main.py
# Calculadora

class Calculadora:
    def __init__(self):
        self.ops = dict(a=self.add, d=self.div, m=self.mul, q=self.no_go)
        self.reg = 0
        self.options = "a"
        self.go = True
        
    def add(self, op):
        return self.reg + op
         
    def div(self, op):
        return self.reg // op
         
    def mul(self, op):
        return self.reg * op
         
    def no_go(self, op):
        return None
        
    def operate(self):
        self.options = str(input('Escolha uma das seguintes operações (m, a, d, q=sair):'))
        if self.options == "q":
            return False
        self.reg = int(input("escolha um número:"))
        # get_ops = input("escolha uma operção (a, d, m):")
        op = int(input("escolha outro número:"))
        if self.options in self.ops:
            res = self.ops[self.options](op)
            input(f" resultado: {res}")
        else:
            input("operação inválida")
        return True
            
    def run(self):
        while self.operate():
            pass
        
        
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
        
        