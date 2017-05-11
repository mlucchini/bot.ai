FROM python:2.7

RUN mkdir /app
WORKDIR /app

COPY botai botai
COPY data data
COPY requirements.txt botai

RUN pip install -r botai/requirements.txt -U
RUN python -m spacy download en

ENV PYTHONPATH $PYTHONPATH:/app

EXPOSE 5000

ENTRYPOINT ["python", "botai/main.py"]
