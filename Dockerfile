FROM python
LABEL maintainer="Fernanda Formiga"

WORKDIR /var/www
COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .