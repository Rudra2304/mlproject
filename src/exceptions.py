# it will contains all the error handling code that is executed if my project raise some error or excpetion.

import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename # it used to get the exception file name 
    error_message='Error occured in python script name [{0}] line number [{1}] error message[{2}]'.format(file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

'''
    here exc_info() will return 3 information but we don't required first 2 of them so we pass it and the 3rd one is required.
    because it will give you the info. about the on which file the exception has occured, on which line has occured etc.. so we store it in 
    one variable called exc_tb.
'''

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
