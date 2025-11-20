class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        #binary search for finding last negative and first positive
        start = 0
        end = len(nums) -1
        num_neg = 0
        num_pos = 0

        while start <= end:
            mid = (end + start) //2
            if nums[mid] < 0:
                start = mid +1
            elif nums[mid] >= 0:
                end = mid -1

        start -= 1

        if start >= 0:
            num_neg = start+1

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (end + start) //2
            if nums[mid] > 0:
                end = mid - 1
            elif nums[mid] <= 0:
                start = mid + 1
        num_pos = len(nums) - start 
        
        return max(num_pos, num_neg)
    