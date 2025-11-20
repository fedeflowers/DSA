class Solution:
    def coloredCells(self, n: int) -> int:
        # res = 1
        # for i in range(1,n):
        #     res+=4*(i-1) +1
        # return res
        return 1 + n* (n-1) * 2