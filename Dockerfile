FROM python:3.7-slim

ENV APP_HOME=/app
WORKDIR \$APP_HOME
COPY app_ner.py requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt
# RUN python3 -m spacy download en_core_web_lg

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD ["python3", "app_ner.py"]
