from user import User
import random #import random variable generator
import string  #import string constants
# import pyperclip


class Credentials:
    '''
    Class to create  account credentials, generate new passwords and save user information
    '''
    
    credential_list = []
    
    def __init__(self,user_name,account_name,password):
        '''
        Method to define the properties for each credentials object.
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        A method that saves new user object
        '''
        Credentials.credential_list.append(self)    

    def delete_credentials(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def check_user(cls,user_name,password):
        '''
        Method that checks if the name and password entered exist in the users_list
        '''
        current_user = ''
        for user in User.user_list:
        	if (user.user_name == user_name and user.password == password):
        		current_user = user.user_name
        return current_user
        