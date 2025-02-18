
{'date': 'Tue Feb 18 2025 15:36:06.270 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  return Elemento(FLORA, w=300 h=300, x=x, y=y, tipo="20% 25%", cena=self.cena)
                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Feb 18 2025 15:36:22.342 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 22
    Lax()
  module <module> line 13
    t = self.sprite(0, 0, 0, 0)
  module <module> line 18
    return Elemento(FLORA, w=300, h=300, x=x, y=y, tipo="20% 25%", cena=self.cena)
AttributeError: 'Lax' object has no attribute 'cena'
'''},