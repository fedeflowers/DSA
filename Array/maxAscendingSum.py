class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        tmp = nums[0]
        res = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                tmp += nums[i]
                res = max(res, tmp)
            else:
                tmp = nums[i]
                
        return res
        