from src.cnnClassifier.components.ModelEval import getmodel__eval
from src.cnnClassifier.config.configuration import ConfigManager


class Model_Eval():
    def __init__(self):
        pass
    def model_eval_start(self):
        model_eval_config=ConfigManager()
        y=model_eval_config.get_model_eval_config()
        evl=getmodel__eval()
        evl.eval_result(y)