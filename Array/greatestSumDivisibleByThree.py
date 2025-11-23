"""
# Explanation of the LeetCode Solution for "Greatest Sum Divisible by Three"

## 1. Brief Explanation of the Approach

The problem is to find the maximum sum of elements from an array `nums` such that the sum is divisible by 3. The solution employs a dynamic programming (DP) approach to tackle this problem efficiently instead of using brute force.

1. **Understanding Remainders**:
   - Since we are interested in sums that are divisible by 3, the main focus is on remainders when the sums are divided by 3.
   - A sum can give one of three possible remainders: 0, 1, or 2.

2. **Dynamic Programming Table**:
   - The DP table `dp` is reduced to an array of size 3, where `dp[r]` (for `r` in [0, 1, 2]) will store the maximum sum that leaves a remainder of `r` when divided by 3 after considering all the numbers processed so far.
   - The base cases are initialized as follows:
     - `dp[0]` is initialized to 0 (because with no elements, the sum is 0, which is divisible by 3).
     - `dp[1]` and `dp[2]` are initialized to negative infinity (indicating that these remainders are not achievable at the start).

3. **Transition Formula**:
   - For each number in `nums`, the algorithm iterates through each of the possible remainders (0, 1, 2) to update the `dp` array. For each remainder `r`, it calculates the previous state that could lead to the current remainder after adding the current number. This utilizes the property of modular arithmetic:
     - `old_rem = (r - (num % 3) + 3) % 3`
   - The transition considers two options: excluding the current number or including it, checking which yields a higher sum.

4. **Final Result**:
   - The solution returns `dp[0]`, which gives the maximum sum of elements from `nums` that is divisible by 3.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of elements in the array `nums`. The algorithm processes each number exactly once and performs a constant amount of work for each number to update the `dp` array (which has a fixed size of 3).

- **Space Complexity**: O(1). The space complexity is constant because the `dp` array has a fixed size of 3, regardless of the input size. We do not need additional data structures that grow with input size.

## 3. Why This Approach is Efficient

- **Reduction from Multiple States to Constant Space**: The approach efficiently reduces the space used by maintaining only the relevant remainders instead of using a full 2D DP table. This optimization helps in managing memory better.
  
- **Avoiding Redundant Calculations**: By using the remainder properties, the algorithm avoids recalculating sums for all possible subsets, which is what would happen in a brute-force approach. Instead, it builds on previously computed values in a systematic way.

- **Speed**: The linear time complexity ensures that the solution can handle large inputs effectively, making it suitable for competitive programming or real-time applications.

Overall, this dynamic programming solution is a sophisticated yet efficient way to solve the problem of finding the greatest sum divisible by three.

Runtime: undefined
Memory: 21700000
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
                old_rem = r - num % 3
                
                # Apply the transition formula
                dp[r] = max(prev_dp[r], prev_dp[old_rem] + num)
                
        return dp[0]


