FROM alpine
WORKDIR /usr/src/cryptocurrency-auto-trader
RUN apk update 
RUN apk add nodejs-current
RUN apk add nodejs-npm
RUN npm install pm2
RUN apk add py-pip
RUN pip install virtualenv 
COPY requirements.txt requirements.txt
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity
RUN virtualenv .env -p python3 
RUN apk add --update --no-cache gcc libxslt-dev
RUN .env/bin/pip install -r requirements.txt
RUN .env/bin/pip install stem && .env/bin/pip install PySocks

RUN apk --update add tor runit tini
COPY service service
RUN chmod +x service/tor/run
COPY torrc /etc/tor/torrc
COPY run-services.sh .

COPY run-server.sh .
COPY process.yaml .
COPY manage.py .
RUN mkdir bitcoin && mkdir cryptocurrency-auto-trader && mkdir data
COPY bitcoin bitcoin
COPY cryptocurrency-auto-trader cryptocurrency-auto-trader
COPY data data

# ENTRYPOINT [".env/bin/python", "manage.py", "runserver", "0.0.0.0:80"]
CMD ["node_modules/pm2/bin/pm2", "start", "process.yaml", "--no-daemon", "--log-date-format", "DD-MM HH:mm:ss.SSS"]