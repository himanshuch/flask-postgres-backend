FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && pip install python-dotenv
COPY . .

EXPOSE 3000
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]