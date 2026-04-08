"""
### Solution Explanation for "Best Time to Buy and Sell Stock"

#### 1. Approach Explanation:
The provided solution uses a single pass through the list of stock prices to determine the maximum profit that can be made by buying and selling the stock. Here’s a breakdown of how it works:

- **Initialization**: 
  - A variable `buy` is initialized to infinity (`float("inf")`), which represents the minimum stock price encountered so far. This ensures that any stock price will be lower during the first iteration.
  - A variable `res` is initialized to 0. This will keep track of the maximum profit found.

- **Iteration**:
  - The algorithm iterates through each price `p` in the `prices` list:
    - If the current price `p` is less than the `buy`, it updates `buy` to the current price. This means the algorithm has found a new lowest price to buy the stock.
    - If the current price `p` is greater than or equal to `buy`, it calculates the profit by subtracting `buy` from `p` and updates `res` if the calculated profit is greater than the current value of `res`.

- **Return Value**: 
  - After iterating through all prices, `res` contains the maximum profit that can be achieved.

#### 2. Time and Space Complexity Analysis:
- **Time Complexity**: O(n)
  - The solution involves a single loop that iterates through the `prices` list once, making the time complexity linear with respect to the number of elements in `prices`.

- **Space Complexity**: O(1)
  - The algorithm uses only a constant amount of additional space (`buy` and `res`), regardless of the input size. Therefore, the space complexity is constant.

#### 3. Efficiency of the Approach:
This approach is efficient due to the following reasons:

- **Single Pass**: By only looping through the prices once, the solution minimizes the number of comparisons and calculations, resulting in an optimal time complexity.
  
- **Constant Space Usage**: The use of a fixed number of variables means that the space required does not grow with input size, making it very memory efficient.

- **Dynamic Tracking of Buy Price**: The algorithm efficiently keeps track of the lowest price seen so far, allowing it to dynamically calculate potential profits without needing nested loops or additional data structures.

Overall, this solution effectively handles the problem in a streamlined manner, making it suitable for large datasets as well.

Runtime: undefined
Memory: 28732000
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        res = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                res = max(res, p - buy)

        return res

