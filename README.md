# Python PostgreSQL CRUD 🚀

Este é um projeto prático que implementa um sistema completo de **CRUD** (Create, Read, Update, Delete) em Python, utilizando o driver **Psycopg2** para se conectar e manipular um banco de dados **PostgreSQL**. O projeto foi estruturado utilizando boas práticas, como o isolamento de credenciais em variáveis de ambiente (`.env`) e organização de código em funções.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **PostgreSQL** (Banco de dados relacional)
* **Psycopg2** (Driver de conexão PostgreSQL para Python)
* **Python-dotenv** (Gerenciamento de variáveis de ambiente)

---

## 📋 Funcionalidades (Operações CRUD)

O script gerencia uma entidade chamada `users` (usuários) e executa o ciclo completo de persistência de dados:

* **Conexão Segura:** Inicialização e fechamento limpo de conexões e cursores.
* **Initialization (Setup):** Criação automática da tabela `users` caso ela não exista (`IF NOT EXISTS`).
* **Create:** Inserção de novos registros com passagem segura de parâmetros (prevenção contra SQL Injection).
* **Read:** Consulta e exibição de todos os registros salvos no banco.
* **Update:** Atualização dinâmica de dados cadastrados (ex: alteração de e-mail).
* **Delete:** Remoção física de registros do banco de dados.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
* Python 3 instalado.
* Instância do PostgreSQL rodando (local ou em container).
* Um banco de dados criado (ex: `crudpython`).

### 2. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio