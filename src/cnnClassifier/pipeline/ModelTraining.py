from src.cnnClassifier.components.ModelTraining import get_final_model
from src.cnnClassifier.config.configuration import ConfigManager





class ModelTraining():
    def __init__(self):
        pass
    def start_training(self):
        model_config=ConfigManager()
        nn=model_config.get_model_Training_config()
        train=get_final_model()
        train.start_traing(nn)
#6th step for model training 
