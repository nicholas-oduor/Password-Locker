import pyperclip
from user import User
from credentials import Credentials
import random #import random variable generator
import string  #import string constants


def create_user(user_name,password):
    '''
    Function to create new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save new user account
    '''
    user.save_user()
    
def verify_user(user_name,password):
    '''
    Function that veryfies the existing user
    
    '''
    check_user = Credentials.check_user(user_name,password)
    return check_user
