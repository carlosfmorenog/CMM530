list_of_passchars = "01"
password_size = 0
while password_size<4: # This while increments the size of the password
    password_size+=1
    indexes = [0]*password_size # create a list to store the indexes to point
    while sum(indexes)<(len(list_of_passchars)-1)*password_size:
        k = ''
        for a in indexes: # This for creates the password based on the values from the list indexes
            k = k + list_of_passchars[a]
        print(k) # add to the salt and test. If true, then return
        # Increment the password vector
        flag = False
        for b, a in enumerate(indexes):
            if a<len(list_of_passchars)-1 and flag == False:
                indexes[b]+=1
                if b>0:
                    for c in range(len(indexes[:b])):
                        indexes[c]=0
                flag = True
    # try the last combination
    k = ''
    for a in indexes: # This for creates the password based on the values from the list indexes
        k = k + list_of_passchars[a]
    print(k) # add to the salt and test. If true, then return