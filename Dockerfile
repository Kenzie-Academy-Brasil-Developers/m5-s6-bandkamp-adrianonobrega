FROM python:3.10

# pra imagem evitar de utilizar os arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

#joga os logs de erro direto pro terminal de logs do container
ENV PYTHONNUNBUFFERED 1


COPY ./requirements.txt .


RUN pip install -U pip
RUN pip install -r requirements.txt

WORKDIR /code

COPY . /code/

# RUN python3 manage.py migrate

# CMD ["python","manage.py","runserver", "0.0.0.0:8000"]