FROM python:3.10-slim-buster
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgrespw
ENV POSTGRES_DB=fastapi_database
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432