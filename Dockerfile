FROM python:3.6
LABEL Name=dockVersion=0.0.1
EXPOSE 8080
WORKDIR /app
ADD . /app
RUN apt-get update
RUN apt-get install build-essential -y --allow-unauthenticated
RUN apt-get install python-dev default-libmysqlclient-dev -y --allow-unauthenticated
RUN apt-get install python3-dev -y --allow-unauthenticated
RUN pip install pipenv
RUN pipenv install  --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "gunicorn", "-t 99999", "-b :8080", "api:__hug_wsgi__","--reload"]
