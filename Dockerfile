FROM python:3.8-alpine
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /code/requirements.txt

WORKDIR /code
RUN pip install -r requirements.txt

COPY . /code
CMD python -m workshop_app.main
