"""
```markdown
## Explanation of the Solution

### 1. Brief Explanation of the Approach
The problem "Mirror Distance of an Integer" requires us to find the distance between a given integer `n` and its mirrored (reversed) version. The solution involves the following steps:

- First, we create a copy of the original integer `n` called `n_copy` to store it before it gets modified.
- We then reverse the number iteratively by extracting its digits from the end. This is done using a while loop that runs as long as `n` is greater than zero:
  - We take the last digit of `n` using `n % 10` and append it to `n_rev` (the reversed number). 
  - We build `n_rev` by multiplying the current `n_rev` by 10 (to make space for the new digit) and adding the last digit of `n`.
  - We then remove the last digit from `n` by performing integer division (`n = n // 10`).
- Finally, the function computes the absolute difference between the original number `n_copy` and the reversed number `n_rev` and returns this value.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of the solution is O(d), where `d` is the number of digits in the integer `n`. This is because we traverse all digits of `n` exactly once while building the reversed number.
  
- **Space Complexity**: The space complexity is O(1), constant space, since we are using a fixed number of variables (`n_rev` and `n_copy`) regardless of the size of `n`. No additional data structures that scale with input size are used.

### 3. Why this Approach is Efficient
This approach is efficient primarily due to its linear traversal of the digits of `n`, allowing us to construct the reversed number without needing to create any intermediate data structures (such as lists or strings) that would take up additional space. The use of simple arithmetic operations avoids unnecessary overhead and leads to optimal performance, particularly for operations that involve modest-sized integers. 

By only requiring a single pass through the digits and leveraging simple operations, this method remains efficient even as the value of `n` increases.
```

Runtime: undefined
Memory: 19192000
"""

# class Solution:
#     def mirrorDistance(self, n: int) -> int:
#         n_rev = int("".join(list(str(n))[::-1]))
#         return abs(n-n_rev)


class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_rev = 0
        n_copy = n
        while n > 0:
            n_rev = n_rev * 10 + n%10
            n = n//10

        return abs(n_copy - n_rev)
        

