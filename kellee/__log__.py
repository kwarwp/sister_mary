
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
{'date': 'Thu Sep 26 2024 15:39:37.62 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
{'date': 'Thu Sep 26 2024 15:49:24.649 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    TextoPortas=(portas_sul, """Fala polly: Rápido! Só temos 3 tentativas!""").vai()
AttributeError: 'tuple' object has no attribute 'vai'
'''},
{'date': 'Thu Sep 26 2024 17:34:48.63 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  TextoIntroducao=Texto(cidadeCharn_norte, """No universo de fantasia das Crónicas Nárnia"""foi=).vai()
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 26 2024 17:34:53.6 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  TextoIntroducao=Texto(cidadeCharn_norte, """No universo de fantasia das Crónicas Nárnia"""foi=).vai()
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 26 2024 17:35:07.783 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  TextoIntroducao=Texto(cidadeCharn_norte, """No universo de fantasia das Crónicas Nárnia"""foi=).vai()
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 26 2024 17:56:25.435 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""" foi=primeiraParte).vai()
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 26 2024 17:56:39.978 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 19
  TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""" foi=primeiraParte).vai()
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 26 2024 17:57:20.468 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  TextoIntroducao=Texto(cidadeCharn_norte,"""No universo de fantasia das Crónicas Nárnia""" foi=primeiraParte).vai()
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Sep 26 2024 18:14:23.498 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    from _spy.vitollino.main import Cena,Sala,Texto,ELemento, STYLE
ImportError: cannot import name 'ELemento'

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
    from _spy.vitollino.main import Cena,Sala,Texto,ELemento, STYLE
'''},
{'date': 'Thu Sep 26 2024 18:14:29.986 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    from _spy.vitollino.main import Cena,Sala,Texto, ELemento, STYLE
ImportError: cannot import name 'ELemento'

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
    from _spy.vitollino.main import Cena,Sala,Texto, ELemento, STYLE
'''},
{'date': 'Tue Oct 01 2024 15:03:12.27 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  LinkPolly = 
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 15:04:33.896 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    cidadeCharn_leste = Cena(IMAGEM_LESTE)
NameError: name 'IMAGEM_LESTE' is not defined
'''},
{'date': 'Tue Oct 01 2024 15:04:48.772 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
    portas_oeste= Cena(IMAGEM_OESTE)
NameError: name 'IMAGEM_OESTE' is not defined
'''},
{'date': 'Tue Oct 01 2024 15:04:55.27 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 27
    historia=Sala(n=cidadeCharn_norte, s=portas_sul, l=cidadeCharn_leste, o=portas_oeste)
NameError: name 'cidadeCharn_leste' is not defined
'''},
{'date': 'Tue Oct 01 2024 15:24:56.487 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  LinkPolly = 
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 15:55:04.691 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 24
  POlly=ELemento(Polly,style=dict(height=60,widht=60, left=600, top=20)
                                                                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 15:58:52.753 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 24
  POlly=ELemento(Polly,style=dict(height=60,widht=60, left=600, top=20)
                                                                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:00:52.169 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 24
  POlly=ELemento(Polly,style=dict(height=60,widht=60, left=600, top=20)Cena = chamada_sul)
                                                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:01:07.8 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  POlly=ELemento(Polly,style=dict(height=60,widht=60, left=600, top=20)Cena = chamada_sul)
                                                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:06:35.869 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 24
  Polly=ELemento(Polly, style=dict(height=60,widht=60, left=600, top=20)Cena = chamada_sul)
                                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:31:08.13 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  polly=ELemento(ElementoPolly,tit="título_do_elemento",
                                                                                                                                                                                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:32:36.854 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly,tit="título_do_elemento",
                                                                                                                                                                                                                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:32:49.342 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly,
                                                                                                                                                               ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 16:33:03.871 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly,
                                                                                                                                                               ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:00:51.606 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly,
                                                                                                                                                               ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:01:11.592 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly,
                                                                                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:01:29.975 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly, style=dict(height=60,widht=60, left=600, top=20),cena = chmada_sul))
                                                                                                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:01:53.710 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  polly = Elemento(ELementoPolly, cena = chmada_sul))
                                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:04:47.447 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 24
  Polly=ELemento(Polly, style=dict(height=60,widht=60, left=600, top=20)Cena = chamada_sul)
                                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:16:04.424 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 20
  Polly = Elemento(ELementoPolly,style=dict(height=60,widht=60, left=600, top=20)
                                                                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:23:23.948 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 21
  Polly = Elemento(ELementoPolly,h=30,w=150, x=600, y=20))
                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Oct 01 2024 17:44:16.59 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 30
    historia=Sala(n=cidadeCharn_norte, l=chamada_sul, s=cidadeCharn_leste, o=portas_oeste)
NameError: name 'cidadeCharn_leste' is not defined
'''},
{'date': 'Tue Oct 01 2024 17:44:31.322 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
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
  module <module> line 30
    historia=Sala(n=cidadeCharn_norte, l=SegundaCena, s=cidadeCharn_leste, o=portas_oeste)
NameError: name 'SegundaCena' is not defined
'''},