# Smart Password Generator generates two types of passwords one is auto generator and other is customized. First I created the class Password to define functions.  Inbuilt random module is used to randomize the sequence.

import random

class Password:
    # Function to generate auto generated password.
    def auto_password():
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        passlen = 8
        p =  "".join(random.sample(s,passlen ))
        return p
    # Function to generate cutomized password.
    def custom_password():
        global char_lst,password_len,char_str
        password_len = int(input(' * Enter a customized password length: '))
        char_lst = []
        char_lst.append(input(' * Enter lowercase characters you want: ').lower())
        char_lst.append(input(' * Enter uppercase characters you want: ').upper())
        char_lst.append(input(' * Enter symbols you want: '))
        char_lst.append(input(' * Enter numbers you want: '))
        char_str = ''
        for char in char_lst:
            char_str+=char
    # Function to randomize custom password.
    def make_custom():
        p =  "".join(random.sample(char_str,password_len ))
        return p
   # Function to take user response for auto generated password.
    def auto_pass_resp():
        autopass = Password.auto_password()
        print('\n * Your Password is: ',autopass)
        try:
            more_auto = input(' * Do you want another combination? (y/n) ')
            if more_auto.lower() == 'y':
                Password.auto_pass_resp()
            elif more_auto.lower() == 'n':
                quit()
            else:
                print('\n * Error! Try Again.')
        except:
            quit()


# Function to take user response for customized password.
    def custom_pass_resp():
        Password.custom_password()
        custompass = Password.make_custom()
        print('\n * Your Password is: ',custompass)
        more_custom = input(' * Do you want another combination? (y/n) ')
        if more_custom.lower() == 'y':
            custompass = Password.make_custom()
            print('\n * Your Password is: ',custompass)
        elif more_custom.lower() == 'n':
            quit()
        else:
            print(' * Error! Try Again. ')

# Main body of program begins here -->

print('\n\n                                * WELCOME TO SMART PASSWORD GENERATOR *\n\n')
try:
    resp = input(' * Which type of password to generate?\n * (AUTO / CUSTOM) \n ')
    if resp.lower() == 'auto':
        Password.auto_pass_resp()
    elif resp.lower() == 'custom':
        Password.custom_pass_resp()
    else:
        print('\n * Something went wrong!')
except:
    print('ERROR! Unexpected input. Try Again.')
    quit()
