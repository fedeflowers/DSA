"""
## Explanation of the Approach

The solution uses a hashmap (dictionary) to keep track of cumulative sums of the elements in the array as it iterates through the array. Here’s a detailed breakdown of the approach:

1. **Cumulative Sum**: As we iterate through the `nums` array, we maintain a cumulative sum, `cum_sum`, that represents the sum of all elements from the start of the array to the current element.

2. **HashMap for Counts**: We use a dictionary `d` to count the occurrences of each cumulative sum encountered. Initially, we insert the cumulative sum of `0` with a count of `1` because a subarray that sums to `k` can be directly equal to `k` if the cumulative sum reaches `k`.

3. **Checking for Subarrays**: For each element in the array, after updating the `cum_sum`, we check if `(cum_sum - k)` exists in our dictionary. If it does, it signifies that there exists a subarray that sums to `k`, ending at the current index. The number of such subarrays is the count associated with `cum_sum - k`.

4. **Updating the Count**: Regardless of whether we found a valid subarray, we also update our dictionary to reflect the new cumulative sum.

5. **Final Output**: The total count of subarrays that sum to `k` is returned.

## Time and Space Complexity Analysis

- **Time Complexity**: 
  - The solution runs in O(n) time, where n is the length of the input array `nums` because we go through the array in a single pass (linear scan).

- **Space Complexity**: 
  - The space complexity is O(n) in the worst case, required for storing the elements in the hashmap. If all cumulative sums are unique, we need to store up to n entries.

## Why This Approach is Efficient

1. **Single Pass**: The approach only requires a single pass over the data to count the valid subarrays, unlike the naive O(n^2) method that involves nested loops and checks the sum over all possible subarrays.

2. **Use of HashMap**: By using a hashmap to store cumulative sums, we can efficiently check for previous sums that would yield the desired sum `k` with constant time complexity O(1) for lookups.

3. **Handles Negative Numbers**: The approach correctly handles cases with negative numbers in the input array, as it relies on cumulative sums rather than direct indices, making it robust for various input scenarios.

Overall, this solution offers an optimal and elegant way to tackle the problem of counting subarrays with a specified sum in a list of integers.

Runtime: undefined
Memory: 22008000
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # res = 0
        # for l in range(n):
        #     for r in range(l+1, n+1):
        #         if sum(nums[l:r]) == k:
        #             res += 1
        # return res
             
        # n = len(nums)
        # res = [0]
        # curr_sum = 0
        # count = 0
        # for el in nums:
        #     curr_sum += el
        #     res.append(curr_sum)
        
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if res[j] - res[i] == k:
        #             count += 1
        # return count
        
        count = 0
        cum_sum = 0
        d = {0:1}
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in d:
                count += d[cum_sum - k]
            d[cum_sum] = d.get(cum_sum, 0) + 1
        return count 
        
        
