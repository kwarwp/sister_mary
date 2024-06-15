
{'date': 'Sat Jun 15 2024 13:25:49.65 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 17
    Cena(Recursos.CENA0, document["pydiv"])
NameError: name 'Recursos' is not defined
'''},
{'date': 'Sat Jun 15 2024 13:37:32.979 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 37
    Jogo()
  module <module> line 34
    Heroi(Recursos.HEROI0, self.jogo)        
  module <module> line 18
    self.heroi = html.DIV(Id="_heroi_", style=dict(
  module <module> line 1
    (self.x)
AttributeError: 'Heroi' object has no attribute 'x'
'''},
{'date': 'Sat Jun 15 2024 13:45:26.301 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  self.legenda = html.DIV("O jogo do Gato",Id="_legenda_)
                                                         ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Sat Jun 15 2024 16:30:37.91 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 51
    Jogo()
  module <module> line 47
    self.cena = Cena(Recursos.CENA1, self)
  module <module> line 14
    self.cena.style.update({"background-image": recurso_cena})
AttributeError: 'CSSProperty' object has no attribute 'update'
'''},
{'date': 'Sat Jun 15 2024 16:40:11.388 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 14
  self.cena = html.DIV(Id="_cena_", style={
                                                                                                                                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Jun 15 2024 16:40:31.35 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 14
  self.cena = html.DIV(Id="_cena_", style={
                                                                                                                                                                                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Jun 15 2024 16:48:08.28 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 27
  self.cena.style.backgroundPosition(f"{self.x}px 0px"})
                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Jun 15 2024 16:48:12.478 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 27
  self.cena.style.backgroundPosition(f"{self.x}px 0px"})
                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Sat Jun 15 2024 16:48:55.792 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 27
  self.cena.style.backgroundPosition = f"{self.x}px 0px"}
                                         ^
SyntaxError: invalid syntax
'''},