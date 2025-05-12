from src.cnnClassifier.components.DataIngesion import datadownload
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import sys
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

class DataIngesionPipeline():
    def __init__(self):
        pass
    def start(self):
        xx=ConfigManager()
        x=xx.get_data()
        b=datadownload()
        m=b.download(x)
        b.unzip(x)
if __name__=='__main__':
    try:
        logging.info(f'data ingestion has  been started')
        mm=DataIngesionPipeline()
        mm.start()
        logging.info(f'data ingestion has been complited')
    except Exception as e:
         logging.info(f"problem in data ingesion")
         raise customexception(e,sys)


#5th upgrade this pipeline file for data ingesion