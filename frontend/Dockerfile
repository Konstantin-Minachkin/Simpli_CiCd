FROM python:3.11
RUN apt-get update && \
    useradd -rm -d /home/run_user/ -p StrongPass@#1 run_user

ADD --chown=run_user ./AnyAsk.py /home/run_user/main_program.py

USER run_user
WORKDIR /home/run_user/