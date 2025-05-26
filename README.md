
# Simulador de Compra de Imóvel - Back-end
# 🚀 API FastAPI com Docker

## ✅ Passos para rodar o projeto:

1. Entre no diretório do projeto:  
```
cd backend
```

2. (Se necessário) Instale o Docker:  
Siga as instruções em [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

3. Suba os containers com Docker:  
```
docker-compose up --build
```

4. Acesse o container para aplicar as migrations:  
```
docker exec -it backend-backend-1 alembic upgrade head
```

5. Acesse a documentação da API (Swagger):  
[http://localhost:8000/docs](http://localhost:8000/docs)
