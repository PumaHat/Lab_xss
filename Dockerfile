FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /srv/
COPY src /srv/src
RUN pip3 install -r requirements.txt
WORKDIR /srv/src

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
