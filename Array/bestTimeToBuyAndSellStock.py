"""
## Solution Explanation for "Best Time to Buy and Sell Stock"

### 1. Approach Explanation
The solution utilizes a single pass through the `prices` list to find the maximum profit that could be made from buying and selling stock. The key idea is to keep track of the minimum stock price encountered so far (`prev_min`) and update the maximum profit (`res`) as we process each price. Here's how the algorithm works:

- Initialize `prev_min` to infinity, which will store the minimum price seen thus far.
- Initialize `res` to zero, which will hold the maximum profit calculated.
- Iterate through each price in the `prices` list:
  - If `prev_min` is not infinity (which it won't be after the first iteration), calculate the potential profit by subtracting `prev_min` from the current price `p`. Update `res` with the maximum value between the existing `res` and the calculated profit.
  - Update `prev_min` to be the minimum of itself and the current price `p`.
- After processing all prices, return the maximum profit.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the number of prices in the `prices` list. This is because we perform a single iteration over the list.
- **Space Complexity**: O(1). We are using a constant amount of space (only a few variables), regardless of the input size since we do not use any additional data structures that grow with input size.

### 3. Efficiency of the Approach
This approach is efficient for several reasons:

- **Single-pass**: It only requires one full scan of the prices list, making it time-efficient. This is a significant advantage over approaches that might involve nested loops, which would increase time complexity to O(N²).
- **Constant space use**: By using just a few variables to track the minimum price and maximum profit, we keep memory usage low, which is often crucial for large inputs.
- **Simple updates**: The operations performed during the iteration involve basic comparisons and arithmetic, which are fast and straightforward.

Overall, this algorithm effectively finds the maximum possible profit from a series of stock prices with minimal computational resources.

Runtime: undefined
Memory: 26860000
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


