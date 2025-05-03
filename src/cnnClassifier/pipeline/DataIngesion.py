from src.cnnClassifier.components.DataIngesion import datadownload
from src.cnnClassifier.config.configuration import ConfigManager

class DataIngesionPipeline():
    def __init__(self):
        pass
    def start(self):
        xx=ConfigManager()
        x=xx.get_data()
        b=datadownload()
        m=b.download(x)
        b.unzip(x)
