FROM python:3.8

ADD web.py .

RUN pip install prometheus_client

CMD ["python", "./web.py"]
