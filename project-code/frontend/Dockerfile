FROM python:3

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

COPY . /src


ENTRYPOINT [ "python" ]

CMD [ "src/main.py" ]
