import os
import logging #import logger
from datetime import datetime #import date and time to create log file name 
log_file=f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log" #file name 
log_path=os.path.join(os.getcwd(),'logs')  #create string with current working directory
os.makedirs(log_path,exist_ok=True) #create log dir
log_file_path=os.path.join(log_path,log_file) #crate log file in log folder



logging.basicConfig(level=logging.INFO,filename=log_file_path,
format=('%(lineno)d--%(levelname)s--%(asctime)s--%(message)s'))  #logging level is info here 