from src.cnnClassifier.logger import logging
from src.cnnClassifier.pipeline.DataIngesion import DataIngesionPipeline
from src.cnnClassifier.pipeline.PrepareBaseModel import PrepareBaseModel
from src.cnnClassifier.pipeline.ModelTraining import ModelTraining
import sys
from src.cnnClassifier.exception import customexception
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

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
    try:
        logging.info(f'trainging has  been started')
        yy=ModelTraining()
        yy.start_training()
        logging.info(f'training has been  complited')
    except Exception as e:
         logging.info(f"problem in training pipeline")
         raise customexception(e,sys)
    
#last step