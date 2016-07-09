#! /usr/bin/env python


def num_to_dig(number):
    """Given a number, return an array with count for each digit"""
    arr = [0 for _ in xrange(10)]
    while number:
        digit = number % 10
        arr[digit] += 1
        number /= 10
    return arr

def check_num(number):
    """Given a number N, check that it has same digits as 2N, 3N, 4N, 5N and 6N"""
    for mult in xrange(2,7):
        if num_to_dig(number) != num_to_dig(number*mult):
            return False

    return True

def solve():
    start = 10
    while True:
        if check_num(start):
            return start
        start += 1

print solve()
