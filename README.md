# Projeto de Autenticação (HTML/JS + FastAPI)

Este é um projeto de estudo demonstrando um fluxo de autenticação simples utilizando um frontend em HTML/CSS/JavaScript puro e um backend em Python com FastAPI.

## Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Backend:** Python, FastAPI, SQLAlchemy
- **Banco de Dados:** SQLite (arquivo local `users.db`)
- **Autenticação:** JWT (JSON Web Tokens) com `python-jose` e `bcrypt`
- **Gerenciamento de Dependências:** Poetry

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.10+](https://www.python.org/)
- [Poetry](https://python-poetry.org/docs/#installation) (Gerenciador de dependências)

## ⚙️ Configuração e Execução

### 1. Backend (API)

Siga os passos abaixo para rodar o servidor da API:

1. **Instale as dependências do projeto:**
   No terminal, dentro da pasta raiz do projeto, execute:

   ```bash
   poetry install
   ```

2. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto (onde está o `pyproject.toml`) e defina uma `SECRET_KEY`. Você pode usar o comando abaixo ou criar criar o arquivo manualmente.

   Conteúdo do arquivo `.env`:

   ```env
   SECRET_KEY=sua_chave_secreta_super_segura_aqui
   ALGORITHM=HS256
   ```

3. **Inicie o servidor:**
   Execute o seguinte comando para iniciar o servidor FastAPI:

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

   O servidor iniciará em `http://127.0.0.1:8000`.

   > **Nota:** O banco de dados `users.db` será criado automaticamente na primeira execução através da função `create_db` no `app/main.py`.

### 2. Frontend

O frontend consiste em arquivos estáticos simples (`index.html`, `register.html`, etc.).

1. **Abra os arquivos no navegador:**
   Você pode simplesmente abrir o arquivo `index.html` no seu navegador.

## 🛠️ Rotas e Funcionalidades

- **Registro (`/register`)**: Criação de novas contas com senha hash (bcrypt).
- **Login (`/login`)**: Autenticação e recebimento de token JWT.
- **Dashboard Protegido**: Página que só pode ser acessada com um token válido (armazenado no localStorage).
- **Verificação de Token (`/auth`)**: Endpoint para validar o token atual.
