# Imagen base liviana con Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY app ./app

# Exponer el puerto
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
