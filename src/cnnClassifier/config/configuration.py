from src.cnnClassifier.constants.cont import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.cnnClassifier.entity.entity import DataIngesion
from box import ConfigBox
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import os
import sys
import yaml

class ConfigManager:
    def __init__(self,configpath=CONFIG_FILE_PATH):
        try:
         self.config=ConfigBox(yaml.safe_load(open(configpath)))  #read yaml and convert it into configbox not dict
         logging.info(f'file has been  lodded')
         #self.params=read_yaml(paramspath)
         os.makedirs(self.config.artifacts_root,exist_ok=True) #create directory
         logging.info(f"{self.config.artifacts_root} has been created")
         os.makedirs(self.config.data_ingestion.root_dir,exist_ok=True)#create directory
         logging.info(f"{self.config.data_ingestion.root_dir} has been created")
        except Exception as e:
         logging.info("yaml file is empty")
         raise customexception(e,sys)
    def get_data(self):
        data_ingesion=DataIngesion(                             #give value of DataIngesion's parameters
            root_dir=self.config.data_ingestion.root_dir,
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir
        )
        return data_ingesion
    
     #3rd  upgrade this config.py file for data ingesion