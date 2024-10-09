FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install poetry poetry-plugin-export \
    && poetry config virtualenvs.in-project true \
    && poetry install \
    && poetry build \
    && poetry export --output requirements.txt \
    && pip install -r requirements.txt \
    && pip install ./dist/*.whl \
    && rm -rf dist/ build/ tests/
CMD ["showtime"]