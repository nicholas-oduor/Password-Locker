import unittest # Importing the unittest module
from user import User
# import pyperclip
from credentials import Credentials

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

    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []   

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credential = Credentials('nicholas','Facebook','123456')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"nicholas")
        self.assertEqual(self.new_credential.account_name,"Facebook")
        self.assertEqual(self.new_credential.password,"123456")

    def test_save_credentials(self):
        '''
        Test to check if the new users info is saved into the user list
        '''
        
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),7)

    def test_delete_credentials(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("nicholas","Facebook","123456") # new credential
        test_credential.save_credentials()

        self.new_credential.delete_credentials()# Deleting a credential object
        self.assertEqual(len(Credentials.credential_list),4)
    
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credentials
        objects to our credential_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("nicholas","Facebook","123456") # new credential
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),9)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)
        
    def test_find_credential_by_account_name(self):
        '''
        test to check if we can find a credential by account_name and display information
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("nicholas","Facebook","123456") # new credential
        test_credential.save_credentials()

        found_credential = Credentials.find_by_account_name("Facebook")

        self.assertEqual(found_credential.account_name,test_credential.account_name)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("nicholas","Facebook","123456") # new credential
        test_credential.save_credentials()

        credential_exists = Credentials.credential_exist("Facebook")

        self.assertTrue(credential_exists)
            
    





if __name__ == '__main__':
    unittest.main()