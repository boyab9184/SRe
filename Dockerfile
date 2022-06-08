FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y python3-pip 

COPY . /app
WORKDIR /app 

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","menu.py"]