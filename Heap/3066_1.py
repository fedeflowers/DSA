class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while len(nums) >= 2 and nums[0] < k:
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)
            heapq.heappush(nums, min(min1, min2) * 2 + max(min1, min2))
            res+=1
        return res