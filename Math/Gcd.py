# Gcd

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a


#SIEVE
#find all primes in seq n
