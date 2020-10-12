FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

CMD uvicorn serve_model:app --host 0.0.0.0 --port 8000