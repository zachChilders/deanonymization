FROM python

ARG ingressconnectionstring
ENV ingressconnectionstring=$ingressconnectionstring

ADD app app
WORKDIR /app/parser

RUN pip3 install -r requirements.txt
#RUN pylint *.py

ENTRYPOINT ["python3", "run_parser.py"]