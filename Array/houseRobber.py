"""
```markdown
# Explanation of the "House Robber" Solution

## 1. Brief Explanation of the Approach
The solution employs a dynamic programming technique to solve the "House Robber" problem. The key idea is to use a `dp` array where `dp[i]` represents the maximum amount of money that can be robbed from the first `i+1` houses.

### Steps:
- **Base Cases**:
  - If there is only one house (`len(nums) == 1`), the maximum amount is simply the value of that house.
  - If there are two houses (`len(nums) == 2`), the maximum is the maximum value of the two houses, as you can't rob both.

- **Recursive Relation**:
  - For more than two houses, the decision at each house `i` is between:
    - Not robbing house `i`, in which case the total is `dp[i-1]`.
    - Robbing house `i`, which means adding the money from house `i` to the maximum amount obtainable from houses up to `i-1` (which is `dp[i-2]`).
  - Therefore, the relation is:  
    `dp[i] = max(dp[i-2] + nums[i], dp[i-1])`
  
- **Final Result**:
  - The answer is found in `dp[-1]`, which gives the maximum money that can be robbed considering all houses.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of this solution is O(N), where N is the number of houses. This is because we iterate through the list of houses once, performing constant-time operations within the loop.

- **Space Complexity**: The space complexity is O(N) due to the `dp` array used to store intermediate results for each house.

## 3. Why this Approach is Efficient
This dynamic programming approach is efficient for several reasons:
- **Optimal Substructure**: The problem can be broken down into smaller subproblems; the decision of robbing each house depends on the solutions of previously solved subproblems.
- **Elimination of Re-computation**: By storing results of the previous computations in `dp`, the same values are not recalculated multiple times, leading to a linear runtime instead of an exponential one.
- **Clear and Scalable**: The logic is simple and can be adapted to other similar "robbery" problems or variants with minor modifications, making it a versatile solution pattern.

In summary, this dynamic programming approach effectively balances between time efficiency and space utilization, making it a well-suited solution for the "House Robber" problem.
```

Runtime: undefined
Memory: 19300000
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]

        
