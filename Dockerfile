

FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["uvicorn", "application:app", "--host", "127.0.0.1", "--port", "3000"]