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

def create_credential(user_name,account_name,password):
    '''
    Function that creates new creadential
    '''
    new_credential = Credentials(user_name,account_name,password)
    return new_credential

def check_existing_account(account_name):
    '''
    Function that checks if ctredential exists
    '''
    return Credentials.find_by_account_name(account_name)
