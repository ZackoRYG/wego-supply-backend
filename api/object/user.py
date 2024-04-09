#Importing Regex for the pattern
import re

#Creating a user class
class User:
    #Creating a constructor with the attritubes of username and password
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #Getting the username
    def get_username(self):
        return self.username

    #Creating a function which sets the username for the user
    def set_username(self, username):

        #This pattern only allows letters and numbers to be part of the username
        username_pattern = r'^[a-zA-Z0-9_]+$'

        #Creating a boolean to see if the password is valid or not
        is_username_valid = False

        #Setting the is_username_valid from the helper method that validates the username 
        is_username_valid = User.validate_input(username ,username_pattern)
        if is_username_valid:
            self.username = username
        else: 
            print("Username is not valid!")

        return is_username_valid

    def set_password(self, password):
        #This is the password pattern
        print(password)
        password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$"
        is_password_valid = False

        #Setting the is_password_valid from the helper method that validates the username 
        is_password_valid = User.validate_input(password, password_pattern)

        if is_password_valid:
            self.password = password
        else: 
            print("Password is not valid")

        return is_password_valid


    #Creating a function to change the old password to a new password
    def change_password(self, old_pass, new_pass):
        if self.password == old_pass:
            self.password = new_pass
            return True
        else:
            return False
        
    #Creating a helper method that checks if the username and password are valid (only uses the characters from the pattern)
        #String - input_string
        #Pattern - Regex String
    def validate_input(input_str, pattern):
        #Creating 
        string_IsValid = False
    # Check if the input matches the pattern
        if re.match(pattern, input_str):
            string_IsValid = True

        return string_IsValid