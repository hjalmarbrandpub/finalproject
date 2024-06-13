FROM python:3.11-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]