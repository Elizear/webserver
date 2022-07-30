FROM python:3.8

ADD web.py .

ADD index.html .

CMD ["python", "./web.py"]
