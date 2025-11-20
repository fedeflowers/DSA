# Multiplication

# bit solution
def multiply(a, b):
    shift = 0
    res = 0
    while b != 0:
        if b & 1 == 1:
            res += a << shift 
        shift += 1
        b = b >> 1
    return res

multiply(20,10)

# recursive solution
def multiply(a, b):
    #a*b = (a//2 * b) + (a//2 * b)
    #a*b = (a//2 * b) + (a//2 * b) + b #a is odd
    sm = min(a,b)
    bg = max(a,b)
    #base case
    def helper(sm, bg):
        if sm == 0:
            return 0
        if sm == 1:
            return bg

        half = sm >> 1 # //2
        half_prod = helper(half, bg)

        if sm % 2 == 0:
            return half_prod + half_prod

        else:
            return half_prod + half_prod + bg

    return helper(sm, bg)


multiply(19,131)