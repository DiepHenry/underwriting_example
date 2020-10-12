FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 80

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt --proxy=avproxy.pacificlife.net:8080 --trusted-host pypi.org

COPY src/ .

CMD uvicorn serve_model:app --host 0.0.0.0 --port 80