from src.cnnClassifier.entity.entity import PrepareBaseModel
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
import os
import sys
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Activation,Input,Dense,Conv2D,MaxPool2D,Flatten,Dropout,BatchNormalization,GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from keras.applications.resnet import ResNet50

class get_model():
  try:
   def get_base_model(self,b:PrepareBaseModel):
    self.base_model_path=(b.base_model_path)
    self.params_weights=b.params_weights
    self.params_include_top=b.params_include_top
    model=ResNet50(weights=self.params_weights,include_top=self.params_include_top) #doenload base model
    model.save(self.base_model_path) #save it
    logging.info("base model has been saved")
    return self.base_model_path ,model.summary()
  except Exception as e:
         logging.info("base model has not been saved")
         raise customexception(e,sys)
  def get_updated_model(self,b:PrepareBaseModel):
   try:
    self.updated_base_model_path=b.updated_base_model_path
    self.base_model_path=os.path.join((b.base_model_path))
    self.base_model=load_model(self.base_model_path)
    self.base_model.trainable=False  #only dense layer's parameters are cont,others will be cont,cont part of model
    model=self.base_model.output  
    model= GlobalAveragePooling2D()(model) #pooling

    model= Dense(1024)(model)
    model= BatchNormalization()(model)
    model= Activation('relu')(model)
    model = Dropout(0.2)(model)

    model= Dense(128)(model)
    model= BatchNormalization()(model)
    model= Activation('relu')(model)
    model= Dropout(0.1)(model)
    
    output= Dense(4, activation='softmax')(model)
    model = Model(inputs=self.base_model.input, outputs=output)
    model.save(self.updated_base_model_path)
    logging.info("updated base model has been saved")
    model.summary()
    return self.updated_base_model_path
   except Exception as e:
         logging.info("updated base model has not been saved")
         raise customexception(e,sys)
  #4thstep for base model