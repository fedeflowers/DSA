# Sieve_of_Eratosthenes

def sieve(n):
    #find primes in a seq of n numbers
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    prime = 2
    while prime*prime < n:
        if primes[prime]:
            for i in range(prime*prime, n+1, prime):
                primes[i] = False
        prime += 1


    return [i for i in range(len(primes)) if primes[i]]
