
# Simulador de Compra de Imóvel - Back-end

# 🚀 API FastAPI com Docker

## ✅ Passos para rodar o projeto:

1. Clone o repositório:  
```
git clone https://github.com/guiszlima/simulation-imovel-api
```

2. Entre no diretório do projeto:  
```
cd simulation-imovel-api/backend
```

3. (Se necessário) Instale o Docker:  
Siga as instruções em [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

4. Copie o arquivo `.env-example` para `.env`:  
```
cp .env-example .env
```

5. (Opcional) Edite o arquivo `.env` caso precise alterar as variáveis de conexão com o banco de dados:  
```
# Caminho para a documentação Swagger
DOCS_PATH="/docs"

# Caminho para a documentação ReDoc
REDOCS_PATH="/redocs"

# Configurações do banco de dados PostgreSQL
POSTGRES_HOST="backend-db-1"
POSTGRES_USER="root"
POSTGRES_PASSWORD="senha"
POSTGRES_PORT=5432
POSTGRES_DB="database"
```

6. Suba os containers com Docker:  
```
docker-compose up --build
```

7. Acesse o container para aplicar as migrations:  
```
docker exec -it backend-backend-1 alembic upgrade head
```

8. Acesse a documentação da API (Swagger):  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Front-end da aplicação:

Para rodar o front-end que consome essa API, acesse:  
[https://github.com/guiszlima/simulation-imovel-frontend](https://github.com/guiszlima/simulation-imovel-frontend)
