import os
import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import render_template,request,Flask


app=Flask(__name__,template_folder='templates/')
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)   #this folder store uploaded images 
@app.route ('/')
def home():
    return render_template('test.html')
@app.route('/pred', methods=['POST'])
def marks():
    os.system("dvc repro")  #here we run our pipeline 
    model_path=os.path.join('artifacts/training','model.h5')
    model=load_model(model_path)
    file=request.files['image']
    file.save(os.path.join('uploads',file.filename))
    file_path=os.path.join('uploads',file.filename)
    image=cv.imread(file_path) #load image
    image=cv.resize(image,(224,224))
    result=np.argmax(model(image.reshape(1,224,224,3)))
    if result==0:
        x='adenocarcinoma'
    elif result==1:
        x='large.cell.carcinoma'
    elif result==2:
        x='normal'
    else:
        x='squamous.cell.carcinoma'
    return f'Predicted Class: {x}'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
    