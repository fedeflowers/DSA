"""
```markdown
## Explanation of the Solution

1. **Approach**

   The problem requires counting the number of "smooth descent periods" in a given list of stock prices. A smooth descent period is defined as a consecutive sequence of descending prices, where each price is exactly 1 less than the previous day's price.

   The solution iterates over the list of prices and keeps track of consecutive descent periods. It uses the following variables:
   - `prev` to store the previous day's price.
   - `series` to count the length of the current descent period.
   - `res` to accumulate the total number of descent periods.

   As we iterate through each price:
   - If the current price is exactly 1 less than the previous price, we increment the `series` counter.
   - If not, we calculate the number of descent periods contributed by the current `series` using the formula \((series + 1) * series / 2\) which counts all the subarrays of lengths 1 through `series` and adds that to `res`. After that, we reset `series`.
   - At the end of the loop, we ensure to add any remaining descent periods contributed by the last series to `res`.

   The formula for descent periods works because if a descent series has a length of `k`, the number of valid subarrays (descent periods) is:
   - Length 1: k choices
   - Length 2: (k-1) choices
   - Length 3: (k-2) choices
   - ...
   - Length k: 1 choice 
   
   This sums up to \(\frac{k(k + 1)}{2}\).

2. **Time and Space Complexity Analysis**

   - **Time Complexity**: The algorithm makes a single pass through the prices list, which takes \(O(n)\), where \(n\) is the length of the prices list. Each operation inside the loop is \(O(1)\). Hence, the overall time complexity is \(O(n)\).

   - **Space Complexity**: The solution uses a fixed amount of extra space (the integer variables `prev`, `series`, and `res`), regardless of the input size. Thus, the space complexity is \(O(1)\).

3. **Why This Approach is Efficient**

   The efficiency of this approach comes from its ability to calculate the number of descent periods in a single pass through the data while maintaining low memory usage. By:
   - Directly processing the input list without using additional data structures (like arrays or lists), it retains space efficiency.
   - Utilizing arithmetic to count subarrays instead of explicitly building or storing all of them, which avoids overhead and keeps the calculations manageable in terms of time complexity.

   This combination of linear time complexity and constant space usage makes the solution optimal for this problem.
```

Runtime: undefined
Memory: 30128000
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev = None
        series = 0
        res = 0
        for el in prices:
            if prev and el == prev - 1:
                series += 1
            else:
                res += ((series + 1) * series) // 2
                series = 0

            prev = el

        return res + len(prices) + ((series + 1) * series) // 2 #last flush
