FROM python:3.8-slim

WORKDIR /app

ENV COSMODB_URI = ""
ENV COSMODB_KEY = ""
ENV COSMODB_NAME = ""
ENV COSMODB_CONTAINER = ""

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
