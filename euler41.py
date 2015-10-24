#!/usr/bin/env python
# -*- coding=utf-8 -*-

import itertools

# find largest pandigital number

# definition taken from wikipedia
# check all numbers up to the square root of n
def isPrime(n):
	for x in xrange(2,int(n**0.5) + 1):
		if n % x == 0:
			return False
			
	return True	

# generate a pan digital number given the number of digits 
def gen_pandigital(max_digits):
	# list of digits
	digits = [x for x in xrange(1, max_digits + 1)]
	# list of corresponding powers of ten
	powers_of_ten = [10**y for y in xrange(max_digits - 1, -1, -1)]
	# make a list of tuple with all possible arrangements of digits
	list_of_unique_digits = [x for x in itertools.permutations(digits)]
	# turns a list of tuples into a list of lists
	list_of_unique_digits = map(list,list_of_unique_digits)
	numbers = [list_of_unique_digits[i][x]*powers_of_ten[x] for i in xrange(len(list_of_unique_digits)) for x in xrange(0,max_digits)]
	super_final = []
	
	for x in xrange(0, len(numbers), max_digits):
		super_final.append(sum(numbers[x:x+max_digits]))
	
	prime_and_pandig = filter(isPrime, super_final)
	return prime_and_pandig

# start from 9 and work your way down
for x in xrange(9,1,-1):
	answers = gen_pandigital(x)
	# take the last element of the first non-empty list and break. Hammertime!
	if answers:
		print "the greatest pandigital prime number is:", answers[-1]
		break
	else:
		pass
