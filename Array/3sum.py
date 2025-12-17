"""
```markdown
# Explanation of the "3Sum" LeetCode Solution

## 1. Brief Explanation of the Approach

The solution to the 3Sum problem leverages the sorted nature of the input array to efficiently find all unique triplets that sum to zero. The main steps involved in the solution are as follows:

1. **Sort the Array**: The input list `nums` is first sorted. This allows us to use a two-pointer technique effectively.
   
2. **Iterate through the Array**: We iterate through the sorted array with an index `i` that represents the fixed element of the triplet.

3. **Skip Duplicates**: For each element at index `i`, we skip the iteration if `nums[i]` is the same as `nums[i-1]` to avoid processing the same number multiple times as the first element of a triplet.

4. **Two-Pointer Technique**: After fixing `nums[i]`, we use two pointers:
   - `l` starts just after `i` (`i + 1`).
   - `r` starts from the end of the array (`n - 1`).
   We calculate the sum of the three elements `total = nums[i] + nums[l] + nums[r]`:
   - If `total` is zero, we have found a valid triplet, which is then added to the result.
   - After finding a valid triplet, both pointers are adjusted to skip over duplicates (moving `l` and `r` inward while their values are the same).
   - If `total` is less than zero, we need a larger number, so we move the left pointer `l` to the right.
   - If `total` is greater than zero, we need a smaller number, so we move the right pointer `r` to the left.

5. **Return Result**: Finally, the result containing all unique triplets that sum to zero is returned.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The overall time complexity of this algorithm is O(n^2). This comes from the O(n log n) time required for sorting the array, followed by an O(n) time for iterating over the array and performing the two-pointer search for each element.

- **Space Complexity**: The space complexity is O(1) (excluding the output). The algorithm uses a constant amount of extra space for variables, and the result is built into a list that is returned.

## 3. Why This Approach is Efficient

- The use of sorting enables the two-pointer technique to efficiently find pairs that, along with the fixed element, sum to zero.
- By skipping duplicates, the algorithm avoids unnecessary calculations and ensures that only unique triplets are considered.
- The two-pointer method significantly reduces the potential number of checks approximately from a cubic complexity (O(n^3) if a naive approach was used) to quadratic (O(n^2)).
- Overall, the combination of sorting and the two-pointer technique results in a highly efficient solution for the 3Sum problem.
```

Runtime: undefined
Memory: 20712000
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for the pointers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res
