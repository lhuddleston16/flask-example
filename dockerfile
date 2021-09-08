FROM python:3.7.9

RUN mkdir -p /usr/src/flask_app/
COPY requirements.txt /usr/src/flask_app/

WORKDIR /usr/src/flask_app/
RUN pip install -r requirements.txt

COPY . /usr/src/flask_app

ENTRYPOINT ["python", "application.py"]
EXPOSE 5000