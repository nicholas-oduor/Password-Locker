from user import User
import random #import random variable generator
import string  #import string constants
import pyperclip


class Credentials:
    '''
    Class to create  account credentials, generate new passwords and save user information
    '''
    
    credential_list = []
    
    def __init__(self,user_name,account_name,password):
        '''
        Method to define the properties for each user object.
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.password = password