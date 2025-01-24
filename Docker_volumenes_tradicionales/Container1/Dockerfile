FROM python:3.13-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY script_resultados.py .
RUN mkdir volumen_compartido
CMD ["python", "script_resultados.py"]
