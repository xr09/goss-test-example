FROM alpine:3.14

ARG APP_HOME=/srv/app

RUN apk add python3 python3-dev py3-pip

RUN adduser -D -g '' flask
RUN mkdir -p ${APP_HOME}
RUN chown flask:flask ${APP_HOME} -R
WORKDIR ${APP_HOME}
COPY --chown=flask:flask src/ ${APP_HOME}/
RUN python3 -m pip install -r requirements.txt

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]
