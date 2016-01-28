#!/usr/bin/env python
# -*- coding=utf-8 -*-

import itertools
import time


# find largest pandigital number

# definition taken from wikipedia
# check all numbers up to the square root of n
def is_prime(n):
    for x in xrange(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False

    return True

# generate a pan digital number given the number of digits
def gen_pandigital(max_digits):
    # list of digits
    digits = [x for x in xrange(1, max_digits + 1)]
    # list of corresponding powers of ten
    powers_of_ten = [10 ** y for y in xrange(max_digits - 1, -1, -1)]
    # make a list of tuple with all possible arrangements of digits
    list_of_unique_digits = [x for x in itertools.permutations(digits)]
    #NEW!
    #sorted list of digits
    list_of_unique_digits_sorted = sorted(list_of_unique_digits, reverse=True)

    #create candidate (starting from highest) and check if it is prime
    for i in xrange(len(list_of_unique_digits_sorted)):
        candidate = 0
        for x in xrange(0, max_digits):
            candidate += list_of_unique_digits_sorted[i][x] * powers_of_ten[x]

        if is_prime(candidate):
            return candidate

    return None

time1 = time.time()
# start from 9 and work your way down
for x in xrange(9, 1, -1):
    answer = gen_pandigital(x)
    # take the last element of the first non-empty list and break. Hammertime!
    if answer is not None:
        print "the greatest pandigital prime number is:", answer
        break

time2 = time.time()

print time2 - time1
