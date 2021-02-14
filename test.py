import unittest # Importing the unittest module
from user import User
import pyperclip

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User('nicholas', '123456')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"nicholas")
        self.assertEqual(self.new_user.password,"123456")
        