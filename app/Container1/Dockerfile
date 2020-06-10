FROM python:3.8

WORKDIR /Register

ADD . /Register

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV NAME Register

CMD ["python","RegisterController.py"]