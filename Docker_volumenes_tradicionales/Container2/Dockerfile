FROM python:3.13-slim
COPY script_noticias.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir volumen_compartido
CMD ["python", "script_noticias.py"]
