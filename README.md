# flask_tests

[Slides](./slides.pdf)

Repositório da palestra "Testes com Flask e #JustPython" na flaskconf 2018
-----------------------------------------------------------------------------
Recomendo que use um virtualenv para fazer isso.

A aplicação foi feita usando `pipenv`, por isso o uso do Pipfile

#### Como instalar tudo?
```sh
pipenv shell
pipenv install
pipenv install -d
```

#### Como rodar os testes?
```
python3 manage.py tests
```

#### Como rodar a aplicação?
```
python3 manage.py runserver
```

#### Como rodar a aplicação com o tox?
```
tox
```

#### Para checar a cobertura?
```
firefox htmlcov/index.html
```
