# -*- coding=utf-8 -*-

# euler 31

list_of_solutions = []
a, b, c, d, e, f, g, h = 1, 2, 5, 10, 20, 50, 100, 200
values = [a, b, c, d, e, f, g, h]
# customize solution to any given number of pence
target = int(raw_input("What amount of money do you want to get in pence? "))
	
# calculates how to get target using coins of different values
def calc(target, values):
	# there is only one solution for 1p target - base case
	if target == 0:
		return 1
	
	# in all other cases - recursive
	# check how make the target out of available coins 
	else:
		
		# calculate how to make the target value minus the coin value, out of coins that are smaller or equal to the target
		solutions = [calc(target - x, [z for z in values if z <= x]) for x in [y for y in values if y <= target]]
		return sum(solutions)
	
		
list_of_solutions = calc(target, values)
	
print "There are {0} ways of combining coins to get {1} pence".format(list_of_solutions, target)
