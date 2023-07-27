FROM python:3.8-slim-buster

WORKDIR /flask_postgre

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 45612

CMD [ "python3", "app.py"]
