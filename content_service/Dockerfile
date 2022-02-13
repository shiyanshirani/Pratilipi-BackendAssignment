FROM python:3.9-buster

ENV PTH /tmp
WORKDIR $PTH

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

# to generate piplock
# copy pipfile
COPY ./Pipfile $PTH/

RUN pipenv install
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./content_service/ $PTH/

EXPOSE 8000

RUN python3 manage.py makemigration
RUN python3 manage.py migrate

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
