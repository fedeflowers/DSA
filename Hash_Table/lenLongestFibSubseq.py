class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        elements = set(nums)
        n = len(nums)
        res = 0

        def fibo(s, e, seq, elements):
            seq.append(e)
            if s + e not in elements :
                if len(seq)<=2:
                    return 0
                return len(seq)

            return fibo(e, s+e, seq, elements)

        for i in range(n):
            for j in range(i+1, n):
                res = max(res, fibo(nums[i], nums[j], [nums[i]], elements))

        return res