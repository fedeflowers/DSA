class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s_i = 0
        s_d = 0
        i = 0
        res = 1
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                res = max(res, i-s_i)
                s_i = i
            if nums[i] >= nums[i-1]:
                res = max(res, i-s_d)
                s_d = i
        res = max(res, i-s_i +1)
        res = max(res, i-s_d +1)
        
        return res