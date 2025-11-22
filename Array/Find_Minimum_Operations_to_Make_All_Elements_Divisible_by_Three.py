"""
## Explanation of the Solution

### 1. Brief Explanation of the Approach
The problem "Find Minimum Operations to Make All Elements Divisible by Three" requires us to determine the minimum number of operations to make every element in a list divisible by 3. The operations that can be performed on each element are adding or subtracting integers.

For each number in the list `nums`, the solution computes the remainder when the number is divided by 3 (i.e., `el % 3`). Depending on the result of `el % 3`, we can determine how far this number is from being divisible by 3.

- If `el % 3 == 0`: The number is already divisible by 3, and no operations are needed.
- If `el % 3 == 1`: We can either subtract 1 (which requires one operation) or add 2 (which requires two operations).
- If `el % 3 == 2`: We can either add 1 (which requires one operation) or subtract 2 (which requires two operations).

The minimum operations needed to make each number divisible by three is therefore the smaller value between `el % 3` and `3 - el % 3`. The solution iterates through each element in `nums`, calculates this minimum for each, and sums it up in `res`, which represents the total number of operations.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The solution has a time complexity of O(N), where N is the number of elements in `nums`. This is because we are iterating through the list of numbers once.
  
- **Space Complexity**: The space complexity is O(1) because we are using a single variable `res` to keep track of the count of operations. We do not use any additional data structures that depend on the input size.

### 3. Why This Approach is Efficient
This approach is efficient for several reasons:

- **Simplicity**: The solution uses a single loop to traverse the input list, making it straightforward and easy to understand.
  
- **Direct Calculation**: By leveraging the properties of modular arithmetic, we avoid unnecessary computations. The solution directly assesses how close each number is to being divisible by 3, allowing it to calculate the required operations immediately.

- **Constant Space Usage**: The algorithm maintains a constant space footprint, which is crucial for handling large inputs efficiently.

Overall, this method efficiently computes the result with minimal computational overhead and is optimal for the problem at hand.

Runtime: undefined
Memory: 18024000
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for el in nums:
            res += min(el%3, 3-el%3)

        return res
