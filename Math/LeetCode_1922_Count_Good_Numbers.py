class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #brute force
        # MOD = 10**9 +7
        # res = 1
        # for i in range(n):
        #     if i % 2 == 0:
        #         res *= 5
        #     else:
        #         res *= 4

        # return res % MOD


        #TLE
        # MOD = 10**9 +7
        # tmp = n // 2
        # res = 20 ** tmp

        # if n % 2 == 1:
        #     res*= 5

        # return res % MOD

######################
        # Exponentiation can be done very fast if we looked at the binary bits of n.
        # MOD = 10**9 + 7

        # # Compute 20^(n // 2)
        # tmp = n // 2
        # res = pow(20, tmp, MOD)  # Using Python's built-in pow with modulus for efficiency

        # # If n is odd, multiply by 5 once more
        # if n % 2 == 1:
        #     res = (res * 5) % MOD

        # return res
            
################## by hand
######### TLE
        # MOD = 10**9 + 7
        
        # def fast_pow(b, exp, MOD):
        #     even = exp % 2 == 0
        #     res = 1
        #     if exp == 0:
        #         return 1
        #     if exp == 1:
        #         return b
            
        #     if exp > 0:
        #         if even:
        #             return fast_pow(b*b, exp//2, MOD) % MOD
        #         else:
        #             return (fast_pow(b*b, exp//2, MOD) * b) %MOD
#         tmp = n // 2
#         res = fast_pow(20, tmp, MOD) 

#         If n is odd, multiply by 5 once more
#         if n % 2 == 1:
#             res = (res * 5) % MOD

#           return res


# ###### ITERATIVE
        # Compute 20^(n // 2)
        MOD = 10**9 + 7
        
        def fast_pow(b, exp, MOD):
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = (res* b) % MOD
                b =  (b*b) % MOD
                exp //= 2

            return res


        # Compute 20^(n // 2)
        tmp = n // 2
        res = fast_pow(20, tmp, MOD) 

        # If n is odd, multiply by 5 once more
        if n % 2 == 1:
            res = (res * 5) % MOD

        return res


        