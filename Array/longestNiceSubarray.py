class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s = 0
        curr_mask = 0
        max_len = 0
        
        for e in range(len(nums)):
            while (curr_mask & nums[e]) != 0:
                # Remove nums[s] from the bitmask and move the left pointer
                curr_mask ^= nums[s]
                s += 1

            # Add nums[e] to the bitmask
            curr_mask |= nums[e]

            # Update max length
            max_len = max(max_len, e - s + 1)
        
        return max_len