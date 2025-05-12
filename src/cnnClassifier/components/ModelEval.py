from src.cnnClassifier.entity.entity import ModelEval
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import os
import sys
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pathlib import Path
import dagshub
import mlflow
from urllib.parse import urlparse


class getmodel__eval():
    try:
        def eval_result(self,j:ModelEval):
             self.model_path=(j.trained_model_path)
             self.EPOCHS=j.EPOCHS
             self.LEARNING_RATE=j.LEARNING_RATE
             self.class_mode=j.class_mode
             self.color_mode=j.color_mode
             self.BATCH_SIZE=j.BATCH_SIZE
             test_datagen=ImageDataGenerator(rescale=1/255) #normalize
             test_data_path = Path("artifacts") / "data_ingestion" / "Data" / "test"
             test_data = test_datagen.flow_from_directory(test_data_path,
             target_size=(224,224),
             color_mode=self.color_mode,
             class_mode=self.class_mode,  #test data generator
             batch_size=self.BATCH_SIZE)
             logging.info("data has been ready for model eval")
             logging.info(f'test data{test_data.class_indices}')
             model=load_model(self.model_path)
             logging.info("model has been  loaded for model eval")
             dagshub.auth.add_app_token('33fa4194997984f4200bf5a3b40710970754c0ce')  #for dagshub authentication
             dagshub.init(repo_owner='arijit99999', repo_name='CNNclassifier', mlflow=True)
             logging.info("dagshub has been  added")
             mlflow.set_registry_uri("https://dagshub.com/arijit99999/CNNclassifier.mlflow") #add url
             logging.info('https://dagshub.com/arijit99999/CNNclassifier.mlflow')
             tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme   #check file data type
             logging.info(f'{tracking_url_type_store}')
             with mlflow.start_run():    #start mlflow tracking
               self.eval=model.evaluate(test_data)
               mlflow.log_param('EPOCHS',self.EPOCHS)
               mlflow.log_param('LEARNING_RATE',self.LEARNING_RATE) #add parameters
               mlflow.log_param('class_mode',self.class_mode)
               mlflow.log_param('BATCH_SIZE',self.BATCH_SIZE)
               mlflow.log_param('optimizer','RMSprop')
               mlflow.log_param('activation','relu')
               mlflow.log_metric("test_loss", self.eval[0])
               mlflow.log_metric("accuracy_score", self.eval[1])
               mlflow.log_metric("precision_score", self.eval[2])  #add matrics
               mlflow.log_metric("recall_score", self.eval[3])
             if tracking_url_type_store != "file":
                 mlflow.keras.log_model(model, "model", registered_model_name="resnet50_model") #if this is not file the save
             else:
                mlflow.keras.log_model(model,"CNNmodel")
             mlflow.end_run()
    except Exception as e:
         logging.info("problem in model evaluation")
         raise customexception(e,sys)