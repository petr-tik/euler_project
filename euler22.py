#!/usr/bin/python

# euler 22

# will add to this in the loop
final_sum = 0

with open('p022_names.txt', 'r') as file:
    # read the file into a string variable    
    read_names = file.read()
    # create a list of names
    names_list = read_names.split('","')
    # sort the list    
    names_list.sort()
    
    # go through every item on the list
    for k in range(len(names_list)):
        # create a list with each character's alphabetic value 
        alph_value = [ord(char) - 64 for char in names_list[k]] 
        # add the product of index (convert to cardinal) and sum of all digits' values for each name
        final_sum += (k + 1)*sum(alph_value)
        
print "The answer is:", final_sum
