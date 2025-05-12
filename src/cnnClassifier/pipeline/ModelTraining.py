from src.cnnClassifier.components.ModelTraining import get_final_model
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import sys




class ModelTraining():
    def __init__(self):
        pass
    def start_training(self):
        model_config=ConfigManager()
        nn=model_config.get_model_Training_config()
        train=get_final_model()
        train.start_traing(nn)
if __name__=='__main__':
    try:
        logging.info(f'trainging has  been started')
        yy=ModelTraining()
        yy.start_training()
        logging.info(f'training has been  complited')
    except Exception as e:
         logging.info(f"problem in training pipeline")
         raise customexception(e,sys)
#6th step for model training 
