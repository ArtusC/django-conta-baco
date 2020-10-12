Exercício prático Nexxera

Prova técnica para programador Python com objtivo de uma criação de uma conta virtual com as funções de débito, crédito e extrato utilizando o framework Django.

Para rodar o projeto:

1) Baixar, via github, o projeto.

2) Extrair o projeto para o diretório de sua preferência.

3) Via CMD, acessar a pasta desafioNex" e criar o ambiente virtual com os comandos:
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

4) Via CMD, instalar na pasta "desafioNex" os frameworks Django e Django REST, com os comandos:
pip install django
pip install djangorestframework

5) Na pasta desafioNex\myapi, rodar o comando (via CMD) para iniciar o acesso ao server:
python manage.py runserver

6) Acessar a URL http://127.0.0.1:8000 para iniciar a aplicação (preferencialmente via Google Chrome).

7) A página inicial contém os links de acesso aos objetios requeridos do projeto:

* Link para acessar a funão de inserção dos débitos, créditos e descrições dos débitos e 
créditos no sistema:
http://127.0.0.1:8000/transacoes/

* Link para acessar a funão de extrato (visualização do saldo inicial e final por transação, podendo 
filtrar a ordenação por crédito ou débito):
http://127.0.0.1:8000/extrato/

* Link para acessar a funão de saldo total (soma de todos os créditos menos a soma de todos os débitos):
http://127.0.0.1:8000/saldo/



