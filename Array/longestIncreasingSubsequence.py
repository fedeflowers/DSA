"""
```markdown
## Explanation of the Longest Increasing Subsequence Solution

### 1. Brief Explanation of the Approach
The solution to the "Longest Increasing Subsequence" (LIS) problem employs an efficient method leveraging binary search, specifically utilizing the `bisect` module in Python to maintain a list that tracks the minimum possible tail values of increasing subsequences of varying lengths.

Here’s a breakdown of the approach:
- We initialize an empty list called `sub` that will store the smallest tail values of increasing subsequences found so far.
- We iterate through each number \( x \) in the input list `nums`:
  - If \( x \) is greater than the last element in `sub` (or if `sub` is empty), we append \( x \) to `sub`.
  - Otherwise, we perform a binary search using `bisect_left` to find the index of the first element in `sub` that is greater than or equal to \( x \). We replace that element with \( x \). This replacement ensures that we maintain the smallest possible tail value for potential increasing subsequences, which allows for more room to build longer subsequences with future elements.
- The final length of the `sub` list at the end of the iteration gives us the length of the longest increasing subsequence.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: \( O(N \log N) \)
  - The algorithm processes each of the \( N \) elements in the `nums` list. For each element, it performs a binary search operation in the `sub` list, which is \( O(\log N) \). Thus, the overall complexity is \( O(N \log N) \).
  
- **Space Complexity**: \( O(N) \)
  - The space used by the `sub` list may grow up to the size of \( N \) (in the worst case where the list is strictly increasing). Hence, the space complexity is \( O(N) \).

### 3. Why This Approach is Efficient
This approach is efficient due to several reasons:
- **Optimal Use of Space**: By maintaining the `sub` list as the smallest possible tail values, the algorithm effectively tracks potential subsequences without exhaustively storing all possible sequences. This optimizes memory usage.
- **Reduced Time Complexity**: The use of binary search significantly reduces the time required to find the appropriate position in the `sub` list for each element, allowing for a much quicker overall solution than the naive \( O(N^2) \) dynamic programming or brute force approaches.
- **Flexibility**: The method can adapt quickly to various input sizes, maintaining performance across different scenarios, making it robust for larger datasets.

Overall, this solution strikes a balance between time efficiency and space management, allowing it to handle larger inputs effectively while providing the correct output.
```

Runtime: undefined
Memory: 18044000
"""

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         #brute force:
#         res = 0
#         def dfs(index, curr_seq):
#             nonlocal res
#             if index >= len(nums):
#                 res = max(res, len(curr_seq))
#                 return
            
#             if 1<=index and curr_seq[-1] < nums[index]:
#                 dfs(index + 1, curr_seq + [nums[index]]) #increase a valid sequence
#             dfs(index + 1, [nums[index]]) #create a new seq
#             dfs(index + 1, curr_seq) #keep trying with old valid seq

#         dfs(0, [nums[0]])
#         return res

#better DP O(n**2)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         @cache
#         def dfs(i, prev_i):
#             if i == len(nums):
#                 return 0
            
#             # Option 1: Skip the current number
#             res = dfs(i + 1, prev_i)
            
#             # Option 2: Include the current number (if valid)
#             # We use prev_i = -1 to denote no previous number chosen yet
#             if prev_i == -1 or nums[i] > nums[prev_i]:
#                 take = 1 + dfs(i + 1, i)
#                 res = max(res, take)
            
#             return res

#         return dfs(0, -1)


#best: 
from bisect import bisect_left
#$O(N \log N)$
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            # If x is greater than the last element, extend the LIS
            if not sub or sub[-1] < x:
                sub.append(x)
            else:
                # Find the first element >= x and replace it
                # This keeps the tails as small as possible to allow future extensions
                idx = bisect_left(sub, x)
                sub[idx] = x
        
        return len(sub)
