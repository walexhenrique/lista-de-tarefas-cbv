# Projeto lista de tarefas

Um projeto de lista de tarefas com autenticação de usuário, criação, edição e exclusão de tarefas. Cujo principais objetivos foram: utilizar Class Based Views e a realização de testes (unitários, de integração e funcionais) mesclando com o conceito de mixins.


***

## Serviços usados
- Github
- Heroku

## Metodologias usadas
- TDD - Desenvolvimento orientado a testes
- Kanban - Metodologia ágil


## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

<ul>
    <li>Versão do python utilizada: 3.10.7</li>
    <li>Versão do django: 4.1.2</li>
</ul>


#### 1 - Passo: Clone
Realize um clone do projeto em seu computador

```
git clone https://github.com/walexhenrique/lista-de-tarefas-cbv.git
```

#### 2 - Passo: Ambiente virtual
Crie um ambiente virtual na pasta <b>raiz</b> do projeto. No seu terminal use:

Comando para a criação do ambiente virtual no Windows:
```
python -m venv venv
```

Comando para a criação do ambiente virtual no Linux:
```
python3 -m venv venv
```

#### 3 - Passo: Ativação do ambiente virtual
Agora você precisa ativar o ambiente virtual para a posterior instalação das dependências do projeto.

Na pasta raiz do projeto, onde você criou o seu ambiente virtual anteriormente. Use:

Comando para a ativação do ambiente virtual no Windows:
```
.\venv\Scripts\activate
```

Comando para a ativação do ambiente virtual no Linux:
```
source venv/bin/activate
```
Se tudo estiver ocorrido bem, terá (venv) em seu <b>terminal!</b>

#### 4 - Passo: Instalação de depedências
É preciso instalar as depedências do projeto para o funcionamento correto. Com o seu ambiente virtual <b>ativo</b> use o comando no seu terminal:

```
pip install -r requirements.txt
```

#### 5 - Passo: Variáveis de ambiente
Para a correta execução do projeto é necessário a configuração das variáveis de ambiente.

* Renomeie o arquivo .env-example para .env

Dentro do arquivo .env (já renomeado), coloque sua PRIMARY KEY do projeto.
```
# /.env

# Django secret key
SECRET_KEY = 'COLOQUE SUA SECRET-KEY AQUI'
```

#### 6 - Passo: Realize as migrações
Para o correto funcionamento do projeto é preciso que seja feito as migrações do banco de dados.

No seu terminal digite:
Windows:
```
python manage.py migrate
```

Linux:
```
python3 manage.py migrate
```

#### 7 - Passo: Executar o projeto
Comando para a execução do projeto no windows:

```
python manage.py runserver
```

Comando para a execução do projeto no linux:

```
python3 manage.py runserver
```

## ⚙️ Executando os testes
Foram realizados diversos testes focando principalmente nas funcionalidades mais ***críticas*** ao sistema.

Comando para a realização dos testes. 
No windows:
```
python manage.py test
```
ou
```
pytest
```

No linux:
```
python3 manage.py test
```

***Atenção***: Caso queira realizar apenas os testes funcionais (Selenium).
```
pytest -m "functional_test"
```

***Atenção***: Caso queira realizar todos os testes menos os funcionais (Selenium).
```
pytest -m "not functional_test"
```

## 🛠️ Construído com

Tecnologias utilizadas na criação desse projeto

* [Django Framework](https://www.djangoproject.com/) - O framework web usado na criação do projeto
* [Pytest](https://docs.pytest.org/en/7.1.x/) - Utilizado na criação dos testes
* [Selenium](https://selenium-python.readthedocs.io/) - Utilizado na automatização dos testes funcionais (versão: Webdriver utilizado no projeto: 106)
* [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - Estruturação da página
* [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - Estilização da página
* [PostgreSQL](https://www.postgresql.org/) - Banco de dados utilizado ao fazer deploy no heroku


## Como usar

### 1 - Quando entrar no site, você vai se deparar com uma tela de login, caso já tenha um usuário cadastro, basta se logar.
![pagina de login](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_inicial.png)

### 2 - Caso não tenha um cadastro no site, crie a sua conta.
![pagina de registro](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_register.png)

### 3 - Ao realizar o cadastro e logar corretamente, você terá acesso ao seu painel de tarefas.
![pagina painel usuário](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_painel.png)

### 4 - Ao clicar em "Criar nova tarefa", você terá acesso à página de criação.
![pagina criar nova tarefa](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_criar_tarefa.png)

### 5 - Finalizado a criação, ela será colocada na sua página de painel, onde lhe permite algumas opções de edição e exclusão.
![pagina painel com tarefa](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_painel_tarefa.png)

### 6 - Ao clicar em "editar tarefa", será apresentado a tarefa a ser editada e você poderá editar o título e o status.
![pagina editar tarefa](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_editar_tarefa.png)

### 7 - Finalizado a edição, ela já estará atualizada em seu painel.
![pagina painel editado](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_painel_editado.png)

### 8 - Ao clicar em "Apagar tarefa", você será levado à página de confirmação.
![pagina confirmação apagar tarefa](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_apagar_tarefa.png)

### 9 - Confirmado a exclusão, você será levado novamente para à página do painel.
![pagina painel apagado](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_painel_apagado.png)

### 10 - Ao possuir muitas tarefas, será habilitado a paginação e apresentará a quantidade de itens de acordo com a escolha de "limite por página".
![pagina painel paginacao](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_paginacao.png)
![pagina painel paginacao 2](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_paginacao_2.png)

### 11 - Ao mudar a opção de "limite por página" para 10, a página utiliza o limite de 10 tarefas por página.
![pagina paginacao limite por página](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_paginacao_escolha.png)

### 12 - Ao clicar em "Sair" você será redirecionado para a página de login e automaticamente estará deslogado da aplicação.
![pagina ao sair](https://github.com/walexhenrique/lista-de-tarefas-cbv/blob/main/.github/pagina_inicial.png)

## Funcionalidades

As principais funcionalidades da aplicação são:
- Criação de tarefas
- Edição de tarefas
- Apagar tarefas
- Registro de usuário
- Login de usuário
- Logout de usuário
- Paginação das tarefas
- Limite de tarefas por página em conjunto com a paginação

## Links
- Deploy no Heroku: https://lista-tarefas-django.herokuapp.com/
- Repositório: https://github.com/walexhenrique/lista-de-tarefas-cbv
    - Em caso de encontrar bugs ou alguma sugestão entre em contato com o meu email: walex999067@gmail.com

## Versionamento
1.0.0.0

## Autor
- **Walex Henrique**
Obrigado pela visita, se curtiu me siga no Github!
