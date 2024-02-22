FROM python:alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /srv/xss

WORKDIR /srv/xss
COPY . /srv/xss
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
