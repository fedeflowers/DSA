"""
```markdown
### Explanation of the Solution

1. **Approach Overview**:
   The goal of the problem is to compute the minimum number of operations required to make all elements in the list `nums` divisible by 3. For each number in the array, we determine how far it is from the nearest multiple of 3. This can be accomplished by calculating the remainder of each element when divided by 3. The remainder can either be 0, 1, or 2.

   - If the remainder is 0 (`el % 3 == 0`), the element is already divisible by 3.
   - If the remainder is 1 (`el % 3 == 1`), you can either subtract 1 (1 operation) or add 2 (1 operation). Both operations require 1 operation in total.
   - If the remainder is 2 (`el % 3 == 2`), you can either subtract 2 (1 operation) or add 1 (1 operation). Again, both operations require 1 operation in total.

   For each element, the minimum operations needed will be `min(el % 3, 3 - el % 3)`, where:
   - `el % 3` calculates how much you would need to add or subtract to reach a multiple of 3.
   - `3 - el % 3` represents the other option for achieving the same result.

   The total number of operations (`res`) is then the sum of these minimum operations across all elements in the input list.

2. **Time and Space Complexity**:
   - **Time Complexity**: `O(N)`, where `N` is the number of elements in `nums`. The solution requires a single pass through the list to compute the minimum operations for each element.
   - **Space Complexity**: `O(1)`, as we are using a constant amount of additional space to store the result (`res`) and do not use any additional data structures that scale with the input size.

3. **Efficiency of the Approach**:
   This approach is efficient due to its linear time complexity, which is optimal for problems requiring examination of all elements in a list. Since we only perform a constant-time calculation for each element, the solution is straightforward and concise. The minimal addition or subtraction needed to reach the nearest multiple intelligently utilizes the modulo operation to dictate the operations. Such analysis allows us to directly compute the required operations based on the properties of numbers, making it both elegant and easy to understand.
```


Runtime: N/A
Memory: N/A
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for el in nums:
            res += min(el%3, 3-el%3)

        return res
