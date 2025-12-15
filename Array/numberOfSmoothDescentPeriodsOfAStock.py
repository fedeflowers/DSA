"""
## Explanation of the Solution for "Number of Smooth Descent Periods of a Stock"

1. **Approach Explanation:**
   The solution iterates through the given list of stock prices to count the number of "smooth descent periods". A smooth descent period is defined as a period in which each subsequent price is exactly one less than the previous price. The algorithm keeps track of two variables:
   - `series`: Counts the ongoing smooth descent period's sequence length.
   - `res`: Accumulates the total number of smooth descent periods found so far.

   As the algorithm iterates through the prices:
   - If the current price is exactly one less than the previous price (`el == prev - 1`), it increments the `series`.
   - If there is a break in the descent (i.e., the condition above is not met), it computes the number of smooth descent periods contributed by the current `series` using the formula `(series + 1) * series // 2`. This calculates the total pairs of prices in the continuous descent (since a series of length `k` contributes `k + (k-1) + ... + 1`).
   - After calculating the contributions of any ended series, it resets the `series` to zero and continues with the new price.
   - After the loop, it ensures to account for any valid series that may still exist at the end of the list.

   The return value combines the accumulated descent periods and also includes the individual prices which each count as a period of 1.

2. **Time and Space Complexity Analysis:**
   - **Time Complexity:** 
     - The algorithm consists of a single loop through the array of prices, making its time complexity O(n), where n is the number of prices in the list.
   - **Space Complexity:**
     - The space complexity is O(1) since it uses a constant amount of extra space for the variables `prev`, `series`, and `res`, regardless of the input size.

3. **Why This Approach is Efficient:**
   - The algorithm efficiently counts descent periods in a single pass through the prices, ensuring linear time complexity. 
   - By directly calculating the contributions of descent periods when a sequence breaks, it eliminates the need for nested loops or additional data structures that would increase both complexity and run time.
   - The use of the arithmetic series formula for counting pairs of prices in a smooth descent period ensures that the solution remains compact and maintains constant space usage, making it optimal for the problem at hand. 

This approach effectively captures all descending periods while remaining efficient in terms of both time and space, thus providing an optimal solution to the problem.

Runtime: undefined
Memory: 29704000
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # [0, 1, 1, 0]
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
