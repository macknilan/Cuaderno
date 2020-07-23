FROM python:2.7

WORKDIR /app

COPY app.py requirements.txt ./
RUN pip install -r requirements.txt
CMD python app.py
EXPOSE 5000
