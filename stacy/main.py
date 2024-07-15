# sister_mary.stacy.main.py
# Calculadora
'''
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
  '''
class Calculadora:
	def __init__(self):
        self.answers = ['m', 'a', 'd']
        self.options = str(input('Escolha uma das seguintes operações (m, a, d):'))
	def run(self):
    	while True:
        	if self.options in self.answers:
                print('Insiraos dois valores:')
                val1 = int(input('valor 1;'))
                val2 = int(input('valor 2;'))
                if self.options == 'm'
                print(val1, '*', val2, '=', val1 * val2)
                if self.options == 'a'
                print(val1, '+', val2, '=', val1 + val2)
                if self.options == 'd'
                print(val1, '/', val2, '=', val1 / val2)
        
        
Calculadora().run()
        
        