"""
Password validation function

This function  validates password so that it doesn't contain any white space
Password must be at least 12 characters
Password format: it must at least include 1 uppercase, 1 lowercase,
 1 digit and 1 special character

"""

import re

def password_validation(password):
    if re.search(r'[\s]', password):
        print('Whitespace found, your password can\'t contain whitespace')
        message='Whitespace found, your password can\'t contain whitespace'
    else:
        if not len(re.findall(r'.{12,}', password)):
            message = 'The the password should be at least 12 characters'
        elif not len(re.findall(r'\d+', password)):
            message = 'The password should contain at least one digit'
        elif not len(re.findall(r'[A-Z]+', password)):
            message = 'The password should contain uppercase letter'
        elif not len(re.findall(r'[_@$\-#%\*\.]+', password)):
            message = 'The password should contain at least one special character'
        else:
            print('success')
            message = 'success'
    return message