FROM python:3.6

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN pip3 install flask-mysql

EXPOSE 5000

CMD python3 app.py
