"""
## Explanation of the Approach

The provided solution to the problem "Sort Integers by The Number of 1 Bits" utilizes a two-step approach:

1. **Counting 1 Bits**: The helper function `_count1` calculates the number of 1 bits (also known as "Hamming weight" or "popcount") in a given integer `x`. It does this using a loop that repeatedly checks the least significant bit of `x` (using `x & 1`), increments a counter if the bit is 1, and then right shifts `x` (using `x >> 1`) to check the next bit until all bits are processed (i.e., `x` becomes 0).

2. **Sorting**: The main function, `sortByBits`, first creates a list of tuples called `representation_1s`, where each tuple holds the count of 1 bits and the corresponding integer from the input `arr`. This list is then sorted based on two keys:
   - The first key is the count of 1 bits.
   - The second key is the integer value itself (this secondary sorting ensures that if two integers have the same number of 1 bits, they will be sorted in ascending order).
   
Finally, the sorted integers are extracted from the tuples and returned as the output.

## Time and Space Complexity Analysis

- **Time Complexity**:
  - Counting 1 bits for each integer takes `O(log x)` time, where `x` is the number. Since this process is performed for all `n` integers in the list, the overall complexity for counting is `O(n log m)`, where `m` is the maximum number in the list.
  - The sort operation takes `O(n log n)`, as it uses Timsort, which is the standard sorting algorithm in Python.
  
Thus, the total time complexity is:
\[ O(n \log m + n \log n) \]
Since `O(n \log n)` grows faster than `O(n \log m)` for large `n`, we can simplify this to:
\[ O(n \log n) \]

- **Space Complexity**:
  - The primary space used is to store the tuples in `representation_1s`, which is `O(n)` for `n` integers.
  
Therefore, the space complexity is:
\[ O(n) \]

## Why this Approach is Efficient

1. **Direct Counting**: The approach efficiently counts the number of 1 bits using bitwise operations, which are typically fast. The use of `x & 1` and `x >> 1` ensures that we are only dealing with the bits of the integer directly.

2. **Tuple Sorting**: Leveraging Python's robust sorting capabilities allows for quick ordering based on multiple criteria using tuple comparisons, which is both readable and efficient.

3. **Optimal Complexity**: The sorting step dominates the complexity, but the overall time complexity of `O(n \log n)` is manageable for a reasonable range of input sizes, making the algorithm practical for a typical competitive programming context.

4. **Readability**: The use of clear function names and list comprehensions helps make the code easy to understand and maintain, which is valuable in software development as it allows for easier debugging and modifications.

Runtime: undefined
Memory: 19480000
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def _count1(x:int):
            res = 0
            while x != 0:
                res += x & 1
                x = x >> 1
            return res
        representation_1s = [(_count1(x), x) for x in arr]
        representation_1s.sort(key=lambda x: (x[0], x[1]))
        return [x[1] for x in representation_1s]

