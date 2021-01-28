FROM ubuntu:latest
MAINTAINER josejuanWSB jose.pena.gomez@wsb.wroclaw.pl
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN apt-get clean
COPY . /service
WORKDIR /service
RUN pip3 install -r requirements.txt
RUN pip3 install -r test_requirements.txt
ENTRYPOINT ["python"]
CMD ["printerService/views.py"]
