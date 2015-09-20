# -*- coding=utf-8 -*-
# euler 30

# solved? I do now know how to check if larger numbers satisfy this requirement? 


# ask the user to input power and upper limit
power = int(raw_input("What power do you want to take each digit to? "))
upper_limit = 1 + int(raw_input("What upper limit do you want to take? "))
 
# a number is 'funny' when the sum of digits to a particular power is the original number 
funny = []

for number in xrange(2, upper_limit):
	# go through each integer in the range
	# for each integer create an array with number's digits	
	# take each digit to the predetermined power
	digits_powered = [digit**power for digit in [int(symbol) for symbol in str(number)]]
	
	if sum(digits_powered) == number:
		print "We have one! {} = sum of digits to the power of {} ".format(number, power)
		
		funny.append(number)
	else:
		pass
		
print funny
print "This is the sum of all such 'funny' numbers:", sum(funny)
		
# This is the sum of all such 'funny' numbers: 443839

		

