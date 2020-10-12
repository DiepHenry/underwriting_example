FROM python:3.8

EXPOSE 8501

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

CMD streamlit run main.py