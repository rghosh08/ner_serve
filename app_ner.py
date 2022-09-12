import kserve
import spacy
from typing import Dict
from presidio_analyzer.analyzer_engine import AnalyzerEngine
from presidio_analyzer.analyzer_request import AnalyzerRequest
"""REST API server for analyzer."""
import json
import logging
import os
from logging.config import fileConfig
from pathlib import Path
from typing import Tuple

spacy.cli.download("en_core_web_lg")

from presidio_analyzer.analyzer_engine import AnalyzerEngine


class CustomModel(kserve.Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name

    def preprocess(self, request: Dict) -> Dict:
        print('preprocess', request)
        data = request['data']
        return data

    def predict(self, request: Dict) -> Dict:
        analyzer = AnalyzerEngine()
        print('predict', request)
        # return [analyzer.analyze(x) for x in request]
        return analyzer.analyze(text=request[0], language='en')

    def postprocess(self, request: Dict) -> Dict:
        print('postprocess', request)
        return {'result': json.dumps(request, default=vars)}

if __name__ == "__main__":
    model = CustomModel("test-custom-model")
    kserve.ModelServer(workers=1).start([model])


