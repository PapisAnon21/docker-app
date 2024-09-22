

FROM python:3.10

#WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

#CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "3000"]
CMD ["python3", "main.py"]