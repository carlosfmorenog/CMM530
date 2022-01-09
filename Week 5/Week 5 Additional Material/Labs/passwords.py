import uuid # uuid is used to generate a random number
import hashlib
 
def hash_password(password):
    salt = uuid.uuid4().hex # Generate a universal unique identifier version 4 and convert it to hexadecimal 
    return hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.md5(salt.encode() + user_password.encode()).hexdigest()
 
stored_pass = input('Please enter a password: ')
hashed_password = hash_password(stored_pass)
print('The hashed password to store is: ' + hashed_password)
new_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, new_pass):
    print('You entered the right password! The salt used was '+hashed_password.split(':')[1])
else:
    print('I am sorry but the password does not match!')
    
    
    
    
    