Exerc�cio pr�tico Nexxera

Prova t�cnica para programador Python com objtivo de uma cria��o de uma conta virtual com as fun��es de d�bito, cr�dito e extrato utilizando o framework Django.

Para rodar o projeto:

1) Baixar, via github, o prjeto desafioNex.

2) Extrair o projeto para o diret�rio de sua prefer�ncia.

3) Via CMD, acessar a pasta desafioNex" e criar o ambiente virtual com os comandos:
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

4) Via CMD, instalar na pasta "desafioNex" os frameworks Django e Django REST, com os comandos:
pip install django
pip install djangorestframework

5) Na pasta desafioNex\myapi, rodar o comando (via CMD) para iniciar o acesso ao server:
python manage.py runserver

6) Acessar a URL http://127.0.0.1:8000 para iniciar a aplica��o (preferencialmente via Google Chrome).

7) A p�gina inicial cont�m os links de acesso aos objetios requeridos do projeto:

* Link para acessar a fun�o de inser��o dos d�bitos, cr�ditos e descri��es dos d�bitos e 
cr�ditos no sistema:
http://127.0.0.1:8000/transacoes/

* Link para acessar a fun�o de extrato (visualiza��o do saldo inicial e final por transa��o, podendo 
filtrar a ordena��o por cr�dito ou d�bito):
http://127.0.0.1:8000/extrato/

* Link para acessar a fun�o de saldo total (soma de todos os cr�ditos menos a soma de todos os d�bitos):
http://127.0.0.1:8000/saldo/



