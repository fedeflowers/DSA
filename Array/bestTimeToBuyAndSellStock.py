"""
```markdown
## Explanation of the LeetCode Solution for "Best Time to Buy and Sell Stock"

### 1. Approach Explanation
The solution uses a single pass through the list of prices to determine the maximum profit that can be made from buying and selling a stock. Here's a breakdown of the method:

- **Initialization**: 
  - `prev_min` is initialized to positive infinity (`float("inf")`) to track the minimum price encountered so far.
  - `res` is initialized to zero to keep track of the maximum profit.

- **Iteration Over Prices**:
  - For each price `p` in the list of `prices`:
    - If `prev_min` is not infinity (which will always be true after the first iteration since `prev_min` will be updated), calculate the profit as `p - prev_min`.
    - Update `res` to be the maximum of its current value and the calculated profit.
    - Update `prev_min` to be the minimum between its current value and the current price `p`.

- **Result**:
  - After iterating through all the prices, `res` contains the maximum profit possible.

This approach leverages the fact that the best time to sell is always after the best time to buy, making it unnecessary to consider all combinations of buy and sell days; instead, you can keep track of only the minimum price seen so far and calculate the profit dynamically.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - The algorithm makes a single pass through the `prices` list, where `N` is the number of elements in the list. Each price is processed in constant time.

- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of extra space, regardless of the input size. Only a few variables (`prev_min` and `res`) are utilized.

### 3. Efficiency of the Approach
This approach is efficient because:
- It traverses the list just once (O(N)) which is optimal for this problem compared to approaches that may involve nested loops (O(N^2)).
- It effectively reduces the problem to maintaining two variables, which results in minimal memory usage.
- The logic is simple and clear, improving code readability and maintainability.

Overall, this solution strikes a perfect balance between efficiency and simplicity, making it a preferred approach for solving the "Best Time to Buy and Sell Stock" problem.
```

Runtime: undefined
Memory: 26852000
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = float("inf")
        res = 0
        for p in prices:
            if prev_min != float("inf"):
                res = max(res, p-prev_min)
            prev_min = min(prev_min, p)
        return res


