from src.cnnClassifier.logger import logging
from src.cnnClassifier.pipeline.DataIngesion import DataIngesionPipeline
from src.cnnClassifier.pipeline.PrepareBaseModel import PrepareBaseModel
import sys
from src.cnnClassifier.exception import customexception

if __name__=='__main__':
    try:
        logging.info(f'data ingestion has  been started')
        mm=DataIngesionPipeline()
        mm.start()
        logging.info(f'data ingestion has been complited')
    except Exception as e:
         logging.info(f"problem in data ingesion")
         raise customexception(e,sys)
    try:
        logging.info(f'download base model has  been started')
        xx=PrepareBaseModel()
        xx.basemodel()
        logging.info(f'download f base model has been  complited')
    except Exception as e:
         logging.info(f"problem in data ingesion")
         raise customexception(e,sys)
    
#last step