from src.cnnClassifier.entity.entity import ModelTraining
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import customexception
from pathlib import Path
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam,RMSprop
from tensorflow.keras.metrics import Precision, Recall
from keras.callbacks import EarlyStopping


class get_final_model():
 try:
  def start_traing(self,p:ModelTraining):
    self.model_path=(p.trained_model_path)
    self.EPOCHS=p.EPOCHS
    self.LEARNING_RATE=p.LEARNING_RATE
    self.class_mode=p.class_mode
    self.color_mode=p.color_mode
    self.BATCH_SIZE=p.BATCH_SIZE
    self.updated_base_model_path=p.updated_base_model_path
    train_datagen=ImageDataGenerator(rotation_range=30,  #create data augumentation
    width_shift_range=0.2,
    height_shift_range=0.2,
    brightness_range=[.1,1],
    shear_range=0.2,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest',
    vertical_flip=True,
    rescale=1/255)
    valid_datagen=ImageDataGenerator(rescale=1/255) #normalize
    train_data_path = Path("artifacts") / "data_ingestion" / "Data" / "train"
    valid_data_path = Path("artifacts") / "data_ingestion" / "Data" / "valid"
    train_data = train_datagen.flow_from_directory(train_data_path,
    target_size=(224,224),
    color_mode=self.color_mode,
    class_mode=self.class_mode,  #train data generator
    batch_size=self.BATCH_SIZE,
    shuffle=True)
    val_data = valid_datagen.flow_from_directory(valid_data_path,
    target_size=(224,224),
    color_mode=self.color_mode,
    class_mode=self.class_mode,  #train data generator
    batch_size=self.BATCH_SIZE)
    logging.info("data has been ready for traing")
    logging.info(f'{train_data.class_indices}')
    model=load_model(self.updated_base_model_path)
    model=load_model(self.updated_base_model_path)
    logging.info("model has been  loaded")
    optimizer = RMSprop(self.LEARNING_RATE)
    model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy',Precision(), Recall()])
    z=EarlyStopping(monitor="val_precision",
    min_delta=0.00001,
    patience=2,
    verbose=0,
    mode="auto",
    baseline=None,
    restore_best_weights=True,
    start_from_epoch=0)
    model.fit(train_data,epochs=self.EPOCHS,validation_data=val_data,callbacks=z)
    return model.save(self.model_path)
 except Exception as e:
         logging.info("problem in traing")
         raise customexception(e,sys)