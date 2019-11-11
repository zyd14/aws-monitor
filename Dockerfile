from selenium/node-firefox-debug

RUN sudo apt update
RUN sudo apt-get -y install python-pip

COPY src/driver.py driver.py
COPY requirements.txt requirements.txt
RUN sudo touch geckodriver.log
RUN sudo chmod 777 geckodriver.log

#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh"]