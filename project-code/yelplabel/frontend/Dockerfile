# For more information about this base image and dockerfile, see
# https://github.com/GoogleCloudPlatform/python-docker
FROM gcr.io/google_appengine/python

RUN virtualenv /env

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN pip install -r /app/requirements.txt

CMD gunicorn -w 4 -b :$PORT main:src
