FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        saqib
COPY . .
ENV PATH="/py/bin:$PATH"
USER saqib
EXPOSE 8000

