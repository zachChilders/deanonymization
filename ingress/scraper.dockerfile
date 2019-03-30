FROM joyzoursky/python-chromedriver:3.7-selenium

ARG ingressconnectionstring
ENV ingressconnectionstring=$ingressconnectionstring

ADD app app
WORKDIR /app/scraper

RUN pip3 install -r requirements.txt
#RUN pylint *.py

ENTRYPOINT ["python3", "run_scraper.py"]