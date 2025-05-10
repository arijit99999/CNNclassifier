from src.cnnClassifier.entity.entity import DataIngesion
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import os
import sys
import gdown
import zipfile
import warnings
warnings.filterwarnings("ignore", category=UserWarning)




class datadownload():
    def download(self,z:DataIngesion):
      try:
        self.z=z
        url=z.source_URL
        os.makedirs(os.path.dirname(z.local_data_file),exist_ok=True)  #download location and file name but it extract only dir name 
        output_path = z.local_data_file 
        gdown.download(url, output_path, quiet=False)  #gdown for download data from google drive
        logging.info(f'file has been  downloaded{url}')
        data=zipfile.ZipFile(z.local_data_file,'r')  #zup data location
        data.extractall(z.unzip_dir) #unzip location
        data.close()
        logging.info(f'file has been  unzip')
      except Exception as e:
         logging.info(f"data is not being downloded")
         raise customexception(e,sys)
    def unzip(self,z:DataIngesion):
       try:
        self.z=z
        loacation=os.path.join('artifacts\data_ingestion','archive.zip')
        data=zipfile.ZipFile(loacation,'r')   #here again we unzip file 
        data.extractall(z.unzip_dir)
        data.close()
        logging.info(f'file has been  unzip')
       except Exception as e:
         logging.info(f"problem with unziping")
         raise customexception(e,sys)
       
#4th upgrade this component file for data ingesion