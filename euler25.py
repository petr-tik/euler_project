# euler 25

# define first 2 terms and the rest of fib seq
a = ""
n = 1
# ask for the number of digits
limit = int(raw_input("How many digits do you want in your fibbonacci term? "))

# recursively define fib 
def fib(n):
    # first 2 terms of fib seq
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1)+fib(n-2)

# until the number of digits is below limits, keep evaluating fib
while len(a) < limit:
    # turns the result into a string, so you can measure length quickly
    a = str(fib(n))
    # iterate
    n += 1
    
# the answer will be (n - 1), cos we add +1 before exiting the loop, so take it away
print "This is the index of the first number consisting of {} digits:".format(limit), (n - 1)
print "The term is:", fib(n-1)    

# really slow
