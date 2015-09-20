# -*- coding=utf-8 -*-

# euler 34

curious = []
# as seen in https://en.wikipedia.org/wiki/Factorion
limit = 1854721 + 1


# recursively define factorial function
def fact(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n*fact(n-1)
		
# use fact(n) to define function which will sum the factorial values of all digits of n
def fact_digits(i):
	# local variable is set to 0
	result = 0
	# if number is 0 - dump, otherwise start the loop
	while i > 0:
		# add the factorial of the last digit to the result
		result += fact(i % 10)
		# cut the last digit off
		i /= 10
	return result

# choose either for loop or list comprehension
# list comprehension is a bit quicker

# for loop
for i in xrange(10, limit):	
	if i == fact_digits(i):
		print "Bingo! {} has a sum of factorial digits equal to itself".format(i)
		curious.append(i)
	else:
		pass

# list comprehension 
curious2 = [i for i in xrange(10, limit) if i == fact_digits(i)]

print "The sum of all curious numbers is: {}".format(sum(curious))
# The sum of all curious numbers is: 40730
