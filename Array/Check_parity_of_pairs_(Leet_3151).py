class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if 0 <= i-1< n :
                if nums[i] % 2 == 0 and nums[i-1] % 2 == 0:
                    return False
                elif nums[i] % 2 != 0 and nums[i-1] % 2 != 0:
                    return False
        return True