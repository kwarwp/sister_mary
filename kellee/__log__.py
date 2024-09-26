
{'date': 'Thu Sep 26 2024 15:17:35.160 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 2
    from _spy.vitollino.main import Cena,Sala, ELement, Texto, STYLE
ImportError: cannot import name 'ELement'

ImportError
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 268
    action()
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 2
    from _spy.vitollino.main import Cena,Sala, ELement, Texto, STYLE
'''},
{'date': 'Thu Sep 26 2024 15:17:47.335 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    cidadeCharn_norte.norte.vai()
AttributeError: 'Cena' object has no attribute 'norte'
'''},
{'date': 'Thu Sep 26 2024 15:18:04.222 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    cidadeCharn.norte.vai()
NameError: name 'cidadeCharn' is not defined
'''},
{'date': 'Thu Sep 26 2024 15:23:31.212 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 18
    historia=Sala(n=cidadeCharn_norte, s=IMAGEM_SUL, L=cidadeCharn_leste, O=portas_oeste)
  module _spy.vitollino.main line 1015
    Sala.c(**kwargs)
  module _spy.vitollino.main line 1043
    setattr(Sala, nome, Sala(nome=nome, **cena))
TypeError: 'Cena' object is not iterable
'''},
{'date': 'Thu Sep 26 2024 15:24:33.992 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 18
    historia=Sala(n=cidadeCharn_norte, s=portas_sul, L=cidadeCharn_leste, O=portas_oeste)
  module _spy.vitollino.main line 1015
    Sala.c(**kwargs)
  module _spy.vitollino.main line 1043
    setattr(Sala, nome, Sala(nome=nome, **cena))
TypeError: 'Cena' object is not iterable
'''},
{'date': 'Thu Sep 26 2024 15:25:18.314 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  from _spy.vitollino.main import Cena,Sala, 
                                             ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Thu Sep 26 2024 15:25:27.712 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 15
    historia=Sala(n=cidadeCharn_norte, s=portas_sul, L=cidadeCharn_leste, O=portas_oeste)
  module _spy.vitollino.main line 1015
    Sala.c(**kwargs)
  module _spy.vitollino.main line 1043
    setattr(Sala, nome, Sala(nome=nome, **cena))
TypeError: 'Cena' object is not iterable
'''},
{'date': 'Thu Sep 26 2024 15:27:03.704 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 15
    historia=Sala(n=cidadeCharn_norte, s=portas_sul, L=cidadeCharn_leste, O=portas_oeste)
  module _spy.vitollino.main line 1015
    Sala.c(**kwargs)
  module _spy.vitollino.main line 1043
    setattr(Sala, nome, Sala(nome=nome, **cena))
TypeError: 'Cena' object is not iterable
'''},
{'date': 'Thu Sep 26 2024 15:38:44.669 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 16
    Textointroducao(cidadeCharn_norte, """No universo de fantasia das Cróicas Nárnia , Polly Plummer, uma aventureira e curiosa garotinha de 11 anos, fica presa na devastada cidade de Charn.
NameError: name 'Textointroducao' is not defined
'''},