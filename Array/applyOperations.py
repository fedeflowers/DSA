class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0

        count_zero = 0
        res = []
        for el in nums:
            if el != 0:
                res.append(el)
            else:
                count_zero += 1
        for i in range(count_zero):
            res.append(0)

        return res
        