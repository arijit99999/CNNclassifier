from src.cnnClassifier.components.PerpareBaseModel import get_model
from src.cnnClassifier.config.configuration import ConfigManager





class PrepareBaseModel():
    def __init__(self):
        pass
    def basemodel(self):
        base_model_config=ConfigManager()
        z=base_model_config.get_model_config()
        basemodel=get_model()
        basemodel.get_base_model(z)
        basemodel.get_updated_model(z)
#5th step for base model

