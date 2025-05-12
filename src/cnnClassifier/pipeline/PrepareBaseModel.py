from src.cnnClassifier.components.PerpareBaseModel import get_model
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import sys




class PrepareBaseModel():
    def __init__(self):
        pass
    def basemodel(self):
        base_model_config=ConfigManager()
        z=base_model_config.get_model_config()
        basemodel=get_model()
        basemodel.get_base_model(z)
        basemodel.get_updated_model(z)
if __name__=='__main__':
    try:
        logging.info(f'download base model has  been started')
        xx=PrepareBaseModel()
        xx.basemodel()
        logging.info(f'download f base model has been  complited')
    except Exception as e:
         logging.info(f"problem in data ingesion")
         raise customexception(e,sys)

#5th step for base model

