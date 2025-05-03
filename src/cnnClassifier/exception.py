import sys 

class customexception(Exception): #here we created custom exception class which inharit from Exception class 
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message  #for error message
        _,_,exc_tb = error_details.exc_info() #extract line no and file name using sys
        
        self.lineno=exc_tb.tb_lineno #for line no
        self.file_name=exc_tb.tb_frame.f_code.co_filename  #for file name 
    

    def __str__(self):
        return f"error has been occured in line no {self.lineno} script file name {self.file_name} and message is {self.error_message}"