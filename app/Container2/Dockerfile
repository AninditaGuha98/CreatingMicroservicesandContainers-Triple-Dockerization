FROM python:3.8

WORKDIR /Login

ADD . /Login

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5001

ENV NAME Login

CMD ["python","LoginController.py"]