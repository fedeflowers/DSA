"""
```markdown
# Explanation of the LeetCode Solution for "Greatest Sum Divisible by Three"

## 1. Approach

The problem requires us to find the maximum sum of elements from the given list `nums` such that the sum is divisible by 3. The solution utilizes dynamic programming to efficiently compute this maximum sum.

### Dynamic Programming Table

We maintain a 1-dimensional array `dp` where:
- `dp[0]` holds the maximum sum that yields a remainder of 0 when divided by 3.
- `dp[1]` holds the maximum sum that yields a remainder of 1 when divided by 3.
- `dp[2]` holds the maximum sum that yields a remainder of 2 when divided by 3.

Initially:
- `dp[0]` is set to 0 (we can achieve a sum of 0 with no elements).
- `dp[1]` and `dp[2]` are initialized to negative infinity (`float('-inf')`) because we haven't considered any elements yet.

### Transition

For each number in `nums`, we:
1. Take a snapshot of the current `dp` state (`prev_dp`).
2. For each possible remainder (0, 1, 2), calculate which previous remainder could lead to the current remainder after adding the current number.
3. Use the relation:
   - `old_rem = (r - num % 3 + 3) % 3` which helps to find the previous state that would allow for the current number to yield a desired remainder.
   - Update the `dp[r]` using the max of including or excluding the current number:
     - `dp[r] = max(prev_dp[r], prev_dp[old_rem] + num)`.
   
Finally, after iterating through all numbers, `dp[0]` will contain the maximum sum that is divisible by 3.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N). The algorithm iterates through the `nums` array once, and for each number, it processes the three possible remainders (0, 1, 2).
  
- **Space Complexity**: O(1). We use a fixed-size array `dp` of size 3, which does not grow with the input size, making the space constant.

## 3. Efficiency of the Approach

This approach is efficient because it reduces the problem's complexity from an exponential brute-force approach (like the knapsack problem, which would take O(2^N)) to a linear one by using dynamic programming principles. Rather than exploring all combinations of elements, it focuses on the remainders when divided by 3, thus limiting the number of states we need to compute and store. Each state is calculated in constant time due to the limited number of possible remainders, allowing the algorithm to scale efficiently even with larger input sizes.
```

Runtime: undefined
Memory: 21752000
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


