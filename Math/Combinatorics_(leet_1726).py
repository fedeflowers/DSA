class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prds = defaultdict(int)
        res = 0
        #create tuples:
        for i in range(n):
            for j in range(i+1, n):
                prds[nums[i] * nums[j]] += 1

        for _, value in prds.items():
            if value > 1:
                #compute combinatorics
                res += math.comb(value, 2) * 8
        return res
            