FROM python:3.8

WORKDIR /LoginStatus

ADD . /LoginStatus

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5002

ENV NAME LoginStatus

CMD ["python","LoginStatusController.py"]