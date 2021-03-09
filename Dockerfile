FROM python:3.9-alpine

COPY twitter/*.py /bot/twitter/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "-m", "twitter"]