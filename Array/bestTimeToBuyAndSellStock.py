"""
## Explanation of the Solution for "Best Time to Buy and Sell Stock"

### 1. Brief Explanation of the Approach

The given solution aims to determine the maximum profit that can be achieved from buying and selling a stock on specific days, based on the provided price list. The key idea is to iterate through the list of stock prices while keeping track of the lowest price encountered so far (`prev_min`). For each price in the list, the algorithm calculates the profit that would be gained if the stock was bought at the lowest price (`prev_min`) and sold at the current price (`p`). The maximum profit found during the iterations is stored in the variable `res`. At the end of the loop, `res` holds the highest profit possible given the prices.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** O(n), where n is the number of days (or length of the `prices` list). The solution performs a single pass through the list, making a constant time check (comparison and assignments) for each price.
  
- **Space Complexity:** O(1). The algorithm uses a constant amount of extra space since it only maintains a few variables (`prev_min` and `res`), regardless of the input size.

### 3. Why This Approach is Efficient

This approach is efficient because it only requires a single pass through the list of prices, and it only uses a small, fixed amount of extra memory. By maintaining a running minimum (`prev_min`) and updating the maximum profit (`res`) dynamically, the algorithm avoids the need for nested loops (which would lead to a time complexity of O(n^2)). Thus, it achieves optimal performance while also being straightforward to understand and implement. This makes it suitable for large inputs, where a more naive approach would falter due to increased time complexity.

Runtime: undefined
Memory: 28576000
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


