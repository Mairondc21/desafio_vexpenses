# desafio_vexpenses_Mairon
Muito prazer meu nome é Mairon o desafio foi concluido com sucesso. Email cadastrado duartemairon@gmail.com

## Instalação com o poetry
1 - Clonar o repositório no github e entrar no vscode
```console
$ git clone https://github.com/Mairondc21/desafio_vexpenses.git
$ cd desafio_vexpenses
$ code .
```
2 - Adicionar e ativar a virtual machine
```console
$ poetry init
$ poetry shell
```
4 - Baixar todas bibliotecas que eu utilizei
```console
$ poetry install
```
5 - Rodar o projeto
```console
$ poetry run python src/main.py
```

## Instalação sem o poetry
1 - Clonar o repositório no github e entrar no vscode
```console
$ git clone https://github.com/Mairondc21/desafio_vexpenses.git
$ cd desafio_vexpenses
$ code .
```
2 - Adicionar e ativar a virtual machine
```console
$ python -m venv .venv
$ source .venv/Scripts/activate
```
4 - Baixar todas bibliotecas que eu utilizei
```console
$ pip install pandas flake8 black isort taskipy
```
5 - Rodar o projeto
```console
$ python src/main.py
```