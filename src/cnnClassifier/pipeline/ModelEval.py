from src.cnnClassifier.components.ModelEval import getmodel__eval
from src.cnnClassifier.config.configuration import ConfigManager
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import sys

class Model_Eval():
    def __init__(self):
        pass
    def model_eval_start(self):
        model_eval_config=ConfigManager()
        y=model_eval_config.get_model_eval_config()
        evl=getmodel__eval()
        evl.eval_result(y)
if __name__=='__main__':
    try:
        logging.info(f'evaluation tracking has  been started')
        uu=Model_Eval()
        uu.model_eval_start()
        logging.info(f'tracking has been  complited')
    except Exception as e:
         logging.info(f"problem in mlflow tracking")
         raise customexception(e,sys)