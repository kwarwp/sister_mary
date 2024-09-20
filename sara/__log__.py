
{'date': 'Fri Sep 20 2024 11:50:29.635 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  print(choice(range(100))
       ^
SyntaxError: Unbalanced bracket (
'''},
{'date': 'Fri Sep 20 2024 12:17:00.608 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 43
    carro.move(pista.inicio)
TypeError: move() missing 1 positional argument: y
'''},
{'date': 'Fri Sep 20 2024 12:55:11.729 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  def dentro(self, x, y)
                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Sep 20 2024 13:23:47.750 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  def encerrou(self, x, y)
                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri Sep 20 2024 13:23:59.221 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''[0, 4] True
(3, 4) 3 True
(3, 0) 7 True
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 75
    carro.manual()
  module <module> line 71
    print("encerrou", pista.encerrou(carro.posicao))
TypeError: encerrou() missing 1 positional argument: y
'''},
{'date': 'Fri Sep 20 2024 13:25:12.4 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''[0, 4] True
(3, 4) 3 True
(3, 0) 7 True
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 76
    carro.manual()
  module <module> line 72
    print("encerrou", pista.encerrou(*carro.posicao))
  module <module> line 32
    return (x0 <= x <= x1) and (y2 <= y <= y3)
NameError: name 'x0' is not defined
'''},