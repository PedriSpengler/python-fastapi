# API CRUD — FastAPI + PostgreSQL

API REST para gerenciamento de usuários, construída com **FastAPI** e **PostgreSQL**, utilizando **psycopg2** para acesso ao banco de dados.

## ✨ Funcionalidades

- ✅ Criar usuário
- ✅ Listar usuários
- ✅ Atualizar e-mail de um usuário
- ✅ Deletar usuário
- ✅ Criação automática da tabela no startup da aplicação
- ✅ Validação de dados com Pydantic

## 🛠️ Tecnologias

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [psycopg2](https://www.psycopg.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Uvicorn](https://www.uvicorn.org/)

## 📁 Estrutura do projeto

```
.
├── database.py       # Conexão e operações CRUD com o PostgreSQL
├── main.py           # Endpoints da API (FastAPI)
├── requirements.txt  # Dependências do projeto
├── .env.example       # Modelo de variáveis de ambiente
└── README.md
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
DB_USERNAME=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=nome_do_banco
```

### 5. Execute a aplicação

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

A tabela `users` é criada automaticamente na primeira execução.

## 📚 Documentação interativa

O FastAPI gera documentação automática assim que o servidor está rodando:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## 🔌 Endpoints

| Método | Endpoint             | Descrição                       |
|--------|-----------------------|----------------------------------|
| POST   | `/users/`              | Cria um novo usuário             |
| GET    | `/users/`              | Lista todos os usuários          |
| PUT    | `/users/{username}`    | Atualiza o e-mail de um usuário  |
| DELETE | `/users/{username}`    | Remove um usuário                |

### Exemplos com `curl`

**Criar usuário**
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"username": "junior", "email": "jrmoci@example.com"}'
```

**Listar usuários**
```bash
curl -X GET "http://127.0.0.1:8000/users/"
```

**Atualizar e-mail**
```bash
curl -X PUT "http://127.0.0.1:8000/users/junior" \
  -H "Content-Type: application/json" \
  -d '{"new_email": "novo@example.com"}'
```

**Deletar usuário**
```bash
curl -X DELETE "http://127.0.0.1:8000/users/junior"
```

## 🗄️ Modelo de dados

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

## 📌 Roadmap

- [ ] Endpoint `GET /users/{username}` para buscar usuário específico
- [ ] Paginação na listagem de usuários
- [ ] Autenticação (JWT)
- [ ] Testes automatizados (pytest)
- [ ] Deploy (Docker + Railway/Render)
