FROM python:3.9.2-slim-buster


WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT [ "python3", "app.py" ]
