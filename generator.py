

#---read in the file
my_file = open('//open_test.txt', 'r+') #update the file path here

def bow(f):
    #---turn the file into a list of words
    my_file = f.read() #make the file a variable
    my_list = my_file.split() #make the variable a list of words
    #print(my_list) #check it works

    #---create the dict
    global my_dict #make this global so in next bit the def can see the dict
    my_dict = {} #create a blank dictionary to write the word list to

    for item in my_list:
        if item in my_dict.keys(): #if the word in the wordlist is already a key in the dictionary then...
            my_dict[item]+=1 #increase the count by one
        else:
            my_dict[item]=1 #add to dictionary and make count 1
    print(my_dict)##check it works
    
bow(my_file)
    
    
def top_word_BOW(n):
    bow_list = [] #making the dictionary a list so create a blank list
    for key, value in n.items(): #for every key/ value in the dictionary..
        vk = (value, key) #store each value and key in opposite order in a variable
        bow_list.append(vk) #write each value and key to the new list

    bow_list = sorted(bow_list) #sort the list
    top_word = bow_list[-1] #create varviable from the last item in the list (which is the now highest dict item)
    top_word = list(top_word) #make that pair a list type
    print ("The most frequent word occuring in the text is:             ", top_word[1]) #print the second item in the ist (i.e., the word)
    print ("The most frequent word occurs the following number of times:", top_word[0])
    
top_word_BOW(my_dict) #call the function

