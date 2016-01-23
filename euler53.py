#!/usr/bin/env python
# -*- coding: utf-8 -*-

#euler 53

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n!/r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are greater than one-million?

"""

import math

# need to use dynamic programming, because it deals with factorials. 

# while making a factorial up to n, need to remember the value of r! and (n-r)!
# also, only calculate up to (n-1)/2 values, because they are simmetrical

def nCr(n,r):
	f = math.factorial
	print f(n)/(f(r)*f(n-r))



for n in xrange(1,10):
	print "now assession n = {}".format(n)
	for r in xrange(1, n):
		nCr(n,r)
