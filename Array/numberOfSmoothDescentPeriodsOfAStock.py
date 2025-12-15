"""
```markdown
## Solution Explanation for "Number of Smooth Descent Periods of a Stock"

### 1. Approach Explanation:
The solution is designed to count the number of smooth descent periods in a list of stock prices. A smooth descent period is defined as a sequence of days where the stock price decreases by exactly 1 unit each day.

- The function initializes two variables: `res` (to hold the total count of descent periods) and `length` (to track the length of the current descent period).
- It iterates through the list of prices starting from the second price. For each price:
  - If the current price is exactly one less than the previous price (`prices[i] == prices[i-1] - 1`), it means a descent period is continuing; hence the `length` of the current descent gets incremented.
  - If the current price does not satisfy this condition, it means the descent has ended, and `length` is reset to 1 as the current price forms a new descent period by itself.
- For every price, the `length` is added to the total `res`, counting both the current period and any preceding periods that it completes.
- Finally, the function returns the total count of descent periods `res`.

### 2. Time and Space Complexity Analysis:
- **Time Complexity: O(N)**  
  The algorithm traverses the list of stock prices a single time, making the time complexity linear with respect to the number of prices, denoted as N.

- **Space Complexity: O(1)**  
  The algorithm uses a constant amount of space, regardless of the input size, as it only utilizes a few integer variables (`res` and `length`) for storing counts.

### 3. Why This Approach is Efficient:
This approach is efficient due to its linear traversal of the input list, allowing it to compute the result in a single pass while maintaining a simple state to track the length of descent periods. The use of a running total (`res`) enables the counting of all periods without needing to store or revisit any previous states, resulting in an optimal memory usage pattern. This makes it suitable for large datasets while avoiding the overhead of nested loops or additional data structures typical in other, less efficient solutions.
```

Runtime: undefined
Memory: 30108000
"""

# class Solution:
#     def getDescentPeriods(self, prices: List[int]) -> int:
#         prev = None
#         series = 0
#         res = 0
#         for el in prices:
#             if prev and el == prev - 1:
#                 series += 1
#             else:
#                 res += ((series + 1) * series) // 2
#                 series = 0

#             prev = el

#         return res + len(prices) + ((series + 1) * series) // 2 #last flush

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 1
        length = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                length += 1
            else:
                length = 1
            res += length
            
        return res
