"""
```markdown
## Explanation of the LeetCode Solution for "Greatest Sum Divisible by Three"

### 1. Brief Explanation of the Approach
The problem requires finding the maximum sum of a subset of numbers from an array such that the sum is divisible by three. The solution utilizes Dynamic Programming (DP) to maintain the maximum sum possibilities based on remainders when divided by 3 (0, 1, and 2). 

Instead of keeping a full DP table, the algorithm maintains a compact array `dp` of size 3, where:
- `dp[0]` stores the maximum sum where the sum is `0 mod 3`
- `dp[1]` stores the maximum sum where the sum is `1 mod 3`
- `dp[2]` stores the maximum sum where the sum is `2 mod 3`

For each number in the input list `nums`, the algorithm updates potential maximum sums by considering both including and excluding each number, adjusting the appropriate remainder. The crucial part of the transition is calculating the previous state of the remainder needed to achieve the current remainder after including the number.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the length of the input array `nums`. The solution iterates through each element of `nums` and performs a constant amount of work for each element (updating the `dp` array).
  
- **Space Complexity**: O(1). The solution employs a fixed-size DP array of length 3 to store the results for the corresponding remainders. Thus, it uses constant additional space, independent of the input size.

### 3. Why This Approach is Efficient
This approach is efficient due to the following reasons:
- **Reduced State Space**: By focusing only on the remainders when dividing by 3, the DP storage is minimized compared to using a full 2D table tracking the index and the remainder. Since the properties of modularity are cyclic, we only need to maintain information about the three possible remainders.
  
- **Dynamic Transition**: The algorithm effectively updates the maximum sums without needing to revisit previous states, relying on the mathematical properties of remainders to efficiently calculate the resulting maximum sums.
  
- **Single Pass through Input**: The solution efficiently processes the input in a single pass rather than recursively evaluating all subsets (as in brute force approaches), yielding significant performance benefits for larger inputs.
```


Runtime: undefined
Memory: 21776000
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


