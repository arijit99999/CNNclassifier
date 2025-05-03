from src.cnnClassifier.logger import logging
from src.cnnClassifier.pipeline.DataIngesion import DataIngesionPipeline
import sys
from src.cnnClassifier.exception import customexception

if __name__=='__main__':
    try:
        logging.info(f'data ingestion has  been started')
        mm=DataIngesionPipeline()
        mm.start()
        logging.info(f'data ingestion has complited')
    except Exception as e:
         logging.info(f"problem in data ingesion")
         raise customexception(e,sys)