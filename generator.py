

#---read in the file
my_file = open('//open_test.txt', 'r+') #update the file path here

def bow(f):
    #---turn the file into a list of words
    my_file = f.read() #make the file a variable
    my_list = my_file.split() #make the variable a list of words
#     print(my_list) #check it works

    #---create the dict
    my_dict = {} #create a blank dictionary to write the word list to

    for item in my_list:
        if item in my_dict.keys(): #if the word in the wordlist is already a key in the dictionary then...
            my_dict[item]+=1 #increase the count by one
        else:
            my_dict[item]=1 #add to dictionary and make count 1
    print(my_dict)##check it works
    
bow(my_file)
    
