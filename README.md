# ner_serve

This repo includes the files related to the named entity recognition using ML.

* docker build -t ner-container
* docker run -p 8080:8080 ner-container
* curl localhost:8080/v1/models/test-custom-model:predict -d '{"data": ["test_text"]}'
