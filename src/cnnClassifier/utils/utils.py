import os
from src.cnnClassifier.exception import customexception
import yaml
from src.cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import sys
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logging.info("yaml file is empty")
        raise customexception(e,sys)
