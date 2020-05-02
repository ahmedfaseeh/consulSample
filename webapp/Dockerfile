FROM python:alpine
WORKDIR /app
RUN pip install flask
COPY ./app.py /app/app.py
ENTRYPOINT [ "python" ]
ARG ver=NA
CMD [ "app.py" ]
