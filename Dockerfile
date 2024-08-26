FROM python:3.12

WORKDIR /usr/app

COPY . .

RUN pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["python3" "src/main.py"]
