class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = 16
        for i in reversed(range(p)):
            if n == 0:
                return True
            if 3 ** i <= n:
                n-= 3 ** i
            
        return n==0
        