FROM python:alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /srv
RUN mkdir /srv/xss

WORKDIR /srv/xss
COPY ./requirements.txt /srv/xss
RUN pip3 install -r requirements.amb

EXPOSE 8000

CMD ["python3", "manage.py", "0.0.0.0:8000"]
