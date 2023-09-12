FROM python:3.11-slim

WORKDIR /app

COPY src/ /app
COPY requirements.txt /app

RUN python3 -m pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "api.py" ]

EXPOSE 5000