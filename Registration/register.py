
import string
from tokenize import String
from filestore import save_data
from send_mail import send_mail
import hashlib

# Initializaton of class
class Registration:
    def __init__(self) -> None:
        self.username=input('Enter your username: ') #input data in python
        self.email=input('Enter your email: ')
        self.full_name=input('Enter your full name: ')
        self.password= input('Enter the password: ')
        self.confirm_password=input('Confirm password: ')
    
    #Function to check whether two passwords match or not
    def check_password(self) -> str:  
        if self.password != self.confirm_password:
            raise Exception("password Mismatch")
        return self.password
    
    #Function for registration of the user
    def register(self):
        self.check_password() 
        self.generate_hash()
        send_mail(self)
        save_data(self)
        print("Your are successfully registered as a user.")
    
    def generate_hash(self) -> str:
        plaintext = self.password.encode()
        d = hashlib.sha256(plaintext)
        self.hash = d.hexdigest()
        return self.hash


user=Registration() #Object Creation of the class
user.register() #Function Calling by an object

    




