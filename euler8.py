# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 20:46:29 2015

@author: Owner
"""

"""need to find a 13 digit sequence, where the product of 13 digits is the greatest"""

"""first find all instances of 0 and split the big NUMBER into string 
then classify strings:   i. those with 13 digits or fewer
                         ii. those with more than 13 digits

"""

NUMBER = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""
strings = NUMBER.split('0')
PRODUCT = 0

def product_of_digits(number):
	"""
	for a given number in string form, return the product of its digits
	"""
	RESULT = 1
	# avoid calculating if 0 is inside the string
	if '0' in number:
		return 0
	else:
		for digit_index in xrange(len(number)):
			RESULT *= int(number[digit_index])
		return RESULT

def sum_of_digits(number):
	"""
	for a given number in string form, return the sum of its digits
	"""
	final_sum = 0
	for digit_index in xrange(len(number)):
			final_sum += int(number[digit_index])
	return final_sum




for string in strings:    
    size = len(string)
    print "assessing string: {} with length {}".format(string, size)
    print "The current biggest product is {}".format(PRODUCT)

    if size <= 13:
        if product_of_digits(string) > PRODUCT:
        	PRODUCT = product_of_digits(string)  

    else:
    	for x in xrange(size - 13):
    		if product_of_digits(string[x:x+13]) > PRODUCT:
    			PRODUCT_string = string[x:x+13]
    			PRODUCT = product_of_digits(PRODUCT_string)
    			


print "The string {} produces the largest product = {}".format(PRODUCT_string, PRODUCT)    
	
