# Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

def subarraySum(nums, k):
    count = 0
    cumulative_sum = 0
    prefix_counts = {0: 1}

    for num in nums:
        cumulative_sum += num
        if cumulative_sum - k in prefix_counts:
            count += prefix_counts[cumulative_sum - k]
        prefix_counts[cumulative_sum] = prefix_counts.get(cumulative_sum, 0) + 1
    return count