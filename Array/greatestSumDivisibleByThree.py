"""
```markdown
## Explanation of the Solution

### 1. Brief Explanation of the Approach

The problem "Greatest Sum Divisible by Three" requires finding the maximum sum of a subset of integers from a given list that is divisible by three. The core idea of the solution employed here is dynamic programming (DP). The approach represents states in terms of the maximum achievable sums that yield specific remainders when divided by three (i.e., 0, 1, and 2).

The DP table (`dp`) is constructed to store the maximum sums that can be achieved using the first `i` numbers for each remainder when divided by three. The transitions of the DP are determined based on two choices for each number:
- **Exclude the number**: In this case, the maximum sum for the current remainder stays the same as the previous state.
- **Include the number**: This involves calculating the required previous state that would generate the current remainder after adding the new number.

The essential transition relationship can be represented as:
- For each number, compute the previous remainder that would yield the current remainder when added (i.e., `old_rem = (current_rem - num % 3 + 3) % 3`). Update the DP table using the maximum between excluding or including the current number.

At the end of the first loop over the numbers, the maximum sum that is divisible by three can directly be found in `dp[0]`.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - Where N is the number of elements in the `nums` list. Since we iterate through the list of numbers once and for each number, we perform operations involving three remainders, the overall time complexity is linear in terms of the input size.
  
- **Space Complexity**: O(1)
  - The space complexity is constant since we only maintain a few integer variables for tracking the maximum sums for the three remainders, rather than a full DP table.

### 3. Why This Approach is Efficient

This approach is efficient because:
- It leverages the properties of modular arithmetic, focusing only on the remainders rather than the sums themselves. This allows drastically reducing the potential space we need to track while maintaining correctness.
- By using a single list (`dp`), we avoid the overhead of constructing a full 2D DP table, which improves memory usage.
- The algorithm processes each number in a single pass (O(N)), ensuring that it is well-suited for larger inputs, while direct inclusion/exclusion approaches would have exponential complexity (like in the brute-force method).
  
Together, these points make the DP approach effective both in terms of speed and memory, ensuring the solution can handle a wide range of input sizes efficiently.
```

Runtime: undefined
Memory: 21588000
"""

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # brutce force is 2^n like knapsack problem 0/1, either take the element or not
        #knapsack already tells me to go for dp possibility, even if i exclude elements divisible by 3, then the remaining is same subproblem, so it's probably DP
        # how do i build DP

        # # brute force
        # def bf(res, index):
        #     if index == len(nums):
        #         if res % 3 == 0:
        #             return res
        #         return 0

        #     include = bf(res+nums[index], index+1) 
        #     exclude = bf(res, index+1)

        #     return max(include, exclude)

        # return bf(0, 0)

        #For DP (or memoization) to work efficiently, we need the inputs to repeat frequently.2index: This ranges from $0$ to $N$.
        #  That's small and manageable.current_sum: This keeps growing and can be very large. Because the sums are almost always unique, we rarely hit the exact same state twice!Since
        #  our final goal is only to check if the total is divisible by 3, do we actually need to store the entire sum in our state, or is there a smaller property of the sum that determines divisibility?
        
        # In each cell dp[index][remainder], we store the maximum sum achievable using the first index numbers that results in that specific remainder
        #remainder1 + reminder2 = 3
        #dp[i][r] = max(dp[i-1][r], dp[i-1][(r - num % 3 + 3) % 3] + num)
        # first = exclude, second = include the current num by going back to complementary remainder

        # FULL DP TABLE
        # n = len(nums)
        # # dp[i][r] = max sum using first 'i' numbers with remainder 'r'
        # # Rows: 0 to n (total n+1 rows)
        # # Cols: 0, 1, 2 (remainders)
        # dp = [[0] * 3 for _ in range(n + 1)]
        
        # # Base Case: With 0 numbers, sum is 0 (remainder 0).
        # # Remainders 1 and 2 are impossible.
        # dp[0][0] = 0
        # dp[0][1] = float('-inf')
        # dp[0][2] = float('-inf')
        
        # for i in range(1, n + 1):
        #     num = nums[i-1]  # Current number
        #     current_rem = num % 3
            
        #     for r in range(3):
        #         # Option 1: Exclude the current number
        #         exclude = dp[i-1][r]
                
        #         # Option 2: Include the current number
        #         # Calculate required previous remainder: (target - current + 3) % 3
        #         old_rem = (r - current_rem + 3) % 3
        #         include = dp[i-1][old_rem] + num
                
        #         dp[i][r] = max(exclude, include)
            
        # return dp[n][0]

        # dp[0] = max sum with remainder 0
        # dp[1] = max sum with remainder 1
        # dp[2] = max sum with remainder 2
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            prev_dp = dp[:] # Snapshot of previous row
            for r in range(3):
                # Calculate which previous remainder (old_rem) would lead to 
                # remainder 'r' if we add 'num'
                old_rem = (r - num % 3 + 3) % 3
                
                # Apply the transition formula
                dp[r] = max(prev_dp[r], prev_dp[old_rem] + num)
                
        return dp[0]


