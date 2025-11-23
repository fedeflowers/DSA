"""
## Explanation of the Approach

The given solution is designed to solve the problem "Greatest Sum Divisible by Three" using dynamic programming. The main objective is to find the maximum sum of elements from the input list `nums` such that this sum is divisible by 3.

### Key Points of the Approach:

1. **Dynamic Programming (DP) Table**: 
   The DP table is represented by an array `dp` where:
   - `dp[0]` holds the maximum sum that gives a remainder of 0 when divided by 3.
   - `dp[1]` holds the maximum sum that gives a remainder of 1 when divided by 3.
   - `dp[2]` holds the maximum sum that gives a remainder of 2 when divided by 3.

2. **Base Case Initialization**: 
   We initialize `dp` with:
   - `dp[0] = 0` (sum of 0 is divisible by 3)
   - `dp[1] = float('-inf')` (there cannot be a valid sum with remainder 1 initially)
   - `dp[2] = float('-inf')` (there cannot be a valid sum with remainder 2 initially)

3. **Transition Process**:
   For each number in `nums`, we look at the `prev_dp`, which is a snapshot of the current state of `dp` before updates:
   - For each possible remainder `r` (0, 1, 2), we calculate the potential previous remainder (`old_rem`) that will result in `r` when adding the current number `num`.
   - Using the formula: 
     \[
     dp[r] = \max(prev\_dp[r], prev\_dp[old\_rem] + num)
     \]
   - This transition ensures that we either take the previous maximum for that remainder or include the current number and use the maximum from the complementary remainder.

4. **Final Output**:
   The answer (i.e., the greatest sum that is divisible by three) is given by `dp[0]` after processing all numbers.

## Time and Space Complexity Analysis

- **Time Complexity**: 
  The algorithm iterates through the list of numbers (`n` elements) and, for each number, goes through three possible remainders (0, 1, 2). Thus, the time complexity is:
  \[
  O(n)
  \]
  
- **Space Complexity**: 
  The space is primarily utilized by the `dp` array which has a fixed size of 3 (to store sums with different remainders). The previous state is stored in `prev_dp`, which is also a fixed size array. Therefore, the space complexity is:
  \[
  O(1)
  \]
  
## Why This Approach is Efficient

1. **Optimized Space Usage**: 
   Instead of using a two-dimensional DP table which grows with the number of elements, this solution reduces space usage to a constant size array of size 3. This optimally utilizes memory while still storing necessary information for all possible states.

2. **Avoiding Redundancy**: 
   The algorithm efficiently calculates the new maximum sums based on previously computed values without recalculating states. This helps in shortening the computation time significantly compared to a naive recursive approach.

3. **Linear Time**: 
   The linear time complexity of the solution makes it feasible to handle large input sizes efficiently, as it processes each number exactly once and leverages a constant number of operations for each number.

4. **Directly Related to Problem Requirements**: 
   The usage of remainders aligns perfectly with the problem's requirement to check divisibility by 3, making this approach both intuitive and appropriate for the task at hand.

Runtime: undefined
Memory: 21664000
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
        #dp[i][r] = max(dp[i-1][r], dp[i-1][r - num % 3] + num)
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
        #         # Calculate required previous remainder: target - current
        #         old_rem = r - current_rem
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
                old_rem = r - num % 3
                
                # Apply the transition formula
                dp[r] = max(prev_dp[r], prev_dp[old_rem] + num)
                
        return dp[0]


