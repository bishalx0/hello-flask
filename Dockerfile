FROM python:3.12-rc-slim-buster

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "src/app.py"]
