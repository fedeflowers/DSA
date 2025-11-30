"""
## Explanation of the Solution for "Make Sum Divisible by P"

### 1. Approach

The goal of the problem is to find the shortest contiguous subarray that can be removed from the list `nums` to make the sum of the remaining elements divisible by `p`.

To achieve this, the solution leverages prefix sums and modular arithmetic. Here’s a breakdown of the approach:

1. **Calculate Total Sum and Target Remainder**:
   - Compute the total sum of the array, `total_sum`, and determine the remainder when it is divided by `p`, called `target_rem`. If `target_rem` is `0`, the entire array is already divisible by `p`, and we return `0`.

2. **Prefix Map Initialization**:
   - Create a dictionary `prefix_map` to store the remainders obtained from prefix sums. The key will be the remainder, and the value will be the latest index where this remainder occurred. To facilitate subarrays that start from index `0`, we initialize `prefix_map` with `{0: -1}`.

3. **Iterate Over the Array**:
   - Loop through the array while maintaining a `curr_rem` which keeps track of the current prefix sum's remainder when divided by `p`.
   - For each element, calculate the required remainder that indicates a previous prefix sum that could potentially make the remaining sum divisible by `p`. This is calculated as: 
     \[
     \text{needed} = (curr\_rem - target\_rem) \mod p
     \]
   - If this `needed` remainder exists in `prefix_map`, it implies that there exists a subarray between the index of `needed` and the current index that, if removed, will make the total sum divisible by `p`. Update `min_len` with the length of this subarray if it's shorter than the previously found lengths.

4. **Update the Prefix Map**:
   - Finally, update `prefix_map` with the current index for the current remainder to continue tracking future subarrays.

5. **Return Result**:
   - If no valid subarray was found (i.e., `min_len` remains its initial value), return `-1`. Otherwise, return `min_len`.

### 2. Time and Space Complexity

- **Time Complexity**: \(O(n)\)
  - The solution involves a single pass through the array, and dictionary operations (insertions and lookups) are on average \(O(1)\).

- **Space Complexity**: \(O(n)\)
  - In the worst case, the `prefix_map` could grow to hold every possible remainder (up to \(p\) distinct values), which could lead to a space complexity of \(O(n)\).

### 3. Efficiency of the Approach

This approach is efficient due to the use of prefix sums and modular arithmetic combined with a hash map. The efficiency is achieved because:

- Instead of checking each possible subarray (which would take \(O(n^2)\)), we can determine necessary conditions in constant time using stored remainders.
- By utilizing a hash map, the algorithm quickly finds previous remainders, reducing the need for nested loops.
- The algorithm runs in a linear time relative to the size of the input, which is optimal for problems involving contiguous subarrays.

This results in a significant performance improvement, especially for larger arrays. The space overhead is manageable and allows quick lookups, thus optimizing the solution overall.

Runtime: undefined
Memory: 38144000
"""

# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
        #brute force:
        # i know that the sum(arr) % p  is what i need to remove,
        # that means if i find a subarray with sum % p == sum(arr) %p than i can remove it to make it divisible by p

        # since they are subarrays i can generate them all in O(n**2)
        
        # remove = sum(nums) % p
        # n = len(nums)
        # res = float("inf")
        # if remove == 0: return 0
        # for i in range(n):
        #     curr_s = nums[i]
        #     if curr_s % p == remove:
        #         return 1 #res = max(res, 1)
        #     for j in range(i+1, n):
        #         curr_s += nums[j]
        #         if curr_s % p == remove:
        #             res = min(res, j-i+1) #len of subarray
                

        # if res == float("inf"):
        #     return -1
        # return res


        # Optimized:
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p
        
        if target_rem == 0:
            return 0
        
        # Map stores {remainder: index} to quickly find the needed prefix
        # Initialize with 0:-1 to handle cases where the subarray starts from index 0
        prefix_map = {0: -1}
        curr_rem = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            curr_rem = (curr_rem + num) % p
            
            # We need a previous prefix such that: (curr_rem - prev_rem) % p == target_rem
            # Rearranged: prev_rem = (curr_rem - target_rem) % p
            needed = (curr_rem - target_rem) % p
            
            if needed in prefix_map:
                min_len = min(min_len, i - prefix_map[needed])
            
            # Update map with current index (overwrite to keep the subarray shortest)
            prefix_map[curr_rem] = i
            
        return min_len if min_len < len(nums) else -1
