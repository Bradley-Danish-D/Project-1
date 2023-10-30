from getpass import getpass as p 
import pickle as pi

A = input("1)Login\n2)sign up:\n")
try:
    with open("login.dat", "rb") as f:
        user_ID = pi.load(f)
except FileExistsError:
    user_ID ={}

def login():
        user_name = input("Enter user name:\n")
        password = p()
        f = open("login.dat", "rb")
        if user_name in user_ID and user_ID[user_name] == password:
            print("OK")
        else:
            print("Invilaid")
                

def sign_up():
    user_name = input("Enter user name:\n")
    password = p()
    user_ID[user_name] = password
    if user_name in user_ID == user_name:
        print("User name aldery taken")
    else:
        try:
            f = open("login.dat", "wb")
            pi.dump(user_ID, f)
            f.close()
        except:
            print("Something went wrong")


if A == "1":
    login()
elif A == "2":
    sign_up()
else:
    print("Error")
