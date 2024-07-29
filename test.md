# Password Storage System
## Overview

It is a basic program which help in understanding the working principal of password and username storage in a website, database, encraption, etc. 

Here is the code:

```py
from getpass import getpass as p
import pickle as pi

print("1) login\n2) sign up\nq or Q Quit")
A = int(input("> "))
try:
    with open("login.dat", "rb") as f:
        user_ID = pi.load(f)
except EOFError:
    user_ID = {}


def login():
    """
    This function handles the login process. It prompts the user to enter their username and password.
    If the username and password match the stored credentials, it prints 'OK' and breaks the loop.
    If the username and password do not match, it prints 'Inlaid' and continues the loop.
    If an error occurs during the process, it prints 'User name not available'.

    Parameters:
    None

    Returns:
    None
    """
    while True:
        user_name = input("Enter user name:\n")
        password = p()
        try:
            if user_name in user_ID and user_ID[user_name] == password:
                print("OK")
                break
            else:
                print("Inlaid")
        except (ValueError, EOFError):
            print("User name not available")


def sign_up():
    """
    This function handles the sign-up process. It prompts the user to enter a new username and password.
    If the username is already taken, it prints 'User name already taken'.
    If the username is available, it stores the new username and password in the 'user_ID' dictionary and saves it to the 'login.dat' file.
    If an error occurs during the process, it prints 'Something went wrong'.

    Parameters:
    None

    Returns:
    None
    """
    user_name = input("Enter user name:\n")
    password = p()
    user_ID[user_name] = password
    if user_name in user_ID:
        print("User name already taken")
    else:
        try:
            f = open("login.dat", "wb")
            pi.dump(user_ID, f)
            f.close()
        except:
            print("Something went wrong")


while True:
    if A == "1":
        login()
    elif A == "2":
        sign_up()
    elif (A == "Q" or "q"):
        break
    else:
        print("Error")
```
## Breakdown

We have seprated the code into two parts sign up & sign in(login).

### Sign up
Here we ask for the usename and password to be entered then check if the usename is taken or not, if it taken then we say the username is taken & tell then to choose another username, if not taken then we take the username and password entered by the user and write it down in a binary file(in this case stored as .dat) using the `pickel` module. Suppose if any of the above process is not carred or there is an error rasied while excuting the code, then we raise an exception using the `try and except` statment.

### Sign in(login)
Here we ask for the username and password for login, since we don't want our password to be public we use the `getpass` module then we specify we want the password function to be imported using ```from getpass import getpass as p``` and defining it as p for a unique identification so that we don't confuse other part of the code. The we check if the username & password is match by pulling the password assined to the username entered by the user. Suppose if the username isn't in the binary file or if the user entered a username that doesn't match the username in the binary file, then we raise an exception.

## Background Process
The slection between login and sign up is done by an `if` statement. The pulling  of file is done by `with open()` statement if it's not opened properply we raise an exception with an `try and except` statment.

# Conclusion

It either take username & password and store in a binary file or it verfiy the if the username & password correct.

# Note

There are some bugs in the above code, I hope to improve in the future.