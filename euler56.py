#!/usr/bin/env python


# for a,b < 100 find a**b with the maximal sum of digits


# sum of digits
def digit_sum(n):
	number = n
	digit_sum = 0
	while number > 0:
		digit_sum += number % 10
		number /= 10

	return digit_sum

