#!/usr/bin/python

# euler 20 

# create a factorial function, all other will be subelements
def fact(n):
    # first 2 elements in any factorial
    product = 1
    k = 2
    
    # calculate the factorial value
    for k in range(1,n):
        # mutliply by k
        product *= k
    # create a list of digits in the number    
    digits = [int(i) for i in str(product)]
    
    # print results
    print "This is factorial of %s" % n
    print product
    
    print "This is the sum of digits of factorial %s" % n
    print sum(digits)
    
fact(100)
