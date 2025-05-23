# Use uma imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requirements para instalar as dependências
COPY requirement.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirement.txt

# Copia todo o código da aplicação para dentro do container
COPY . .

# Expõe a porta padrão do FastAPI (uvicorn)
EXPOSE 8000

# Comando para rodar a migration Alembic e depois iniciar o uvicorn
CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]
