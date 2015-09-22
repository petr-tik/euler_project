# -*- coding=utf-8 -*-

upper_limit = int(raw_input("What is the upper limit? "))
base = int(raw_input("Base to convert to: "))

# first find out all palindrome in binary system
# then turn all of them into binary and find out if palindromes in binary

# general converter
def convert(number, base):
	remainder = []
	while number > 0:
		remainder.append(int(number % base))
		number /= base
	# [::-1] reverses the list  
	digits_in_order = remainder[::-1]
	s = reduce(lambda x,y: x+str(y), digits_in_order, '')
	num = int(s)
	return num

# finds all decimal palindromes between 1 and upper limit
decimal_palindromes = [n for n in xrange(1, upper_limit) if n == int(str(n)[::-1])]	

# now convert all decimal palindromes into binary
binary_from_dec = [convert(n,base) for n in decimal_palindromes]

# check for palindromes from binary
binary_palindromes = [n for n in binary_from_dec if n == int(str(n)[::-1])]

solutions = [int(str(n),2) for n in binary_palindromes]

# that way you have a subset of a subset
print "The sum of solutions is: ", sum(solutions)

# The sum of solutions is:  872187
