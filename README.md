# HabitFlow API

API para controle de hábitos desenvolvida com FastAPI e SQLite.

## Como rodar o projeto no Windows

### 1. Criar o ambiente virtual

python -m venv venv

### 2. Ativar o ambiente virtual no CMD

venv\Scripts\activate

### 3. Instalar as dependências

pip install -r requirements.txt

### 4. Rodar a API

uvicorn app.main:app --reload

## Rodar novamente depois da primeira instalação no CMD

venv\Scripts\activate
uvicorn app.main:app --reload
