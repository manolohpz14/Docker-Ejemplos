FROM python:3.13-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY script.py .

ENTRYPOINT ["python", "script.py"]
