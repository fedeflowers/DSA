"""
```markdown
# Explanation of the LeetCode Solution for "Sort Integers by The Number of 1 Bits"

## 1. Brief Explanation of the Approach
The problem is to sort a list of integers based on the number of `1` bits in their binary representation. If two integers have the same number of `1` bits, they should be sorted by their integer value.

The provided solution utilizes Python's built-in list sorting capabilities. Specifically, it leverages the `bit_count()` method introduced in Python 3.10, which efficiently counts the number of `1` bits in an integer.

The approach can be summarized as follows:
- The list `arr` is sorted in place using the `sort()` method.
- The sorting key is a tuple `(x.bit_count(), x)`, where:
  - `x.bit_count()` gives the number of `1` bits in the binary representation of element `x`.
  - `x` provides the tie-breaking criterion in case two numbers have the same number of `1` bits.

After sorting, the list will have all integers arranged first by their number of `1` bits and then by their value in case of ties.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N log N)
  - The primary operation here is sorting the array which takes O(N log N) time, where N is the number of elements in the array. Counting bits using `bit_count()` is performed in constant time, O(1), for each element during the sorting key calculation.

- **Space Complexity**: O(1)
  - The sorting is done in place; thus, the additional space used is minimal, not accounting for the input list itself. The space complexity remains O(1) during the sorting process.

## 3. Why This Approach is Efficient
- **Utilization of Built-in Functions**: The `bit_count()` method is optimized and runs in constant time for practical input sizes, making it faster than manually counting bits through bitwise operations. This reduces the overhead of implementing a custom function to count bits.
  
- **In-place Sorting with Python's Timsort**: Python's sorting algorithm, Timsort, is very efficient in real-world scenarios. It takes advantage of existing order in the data, which might lead to faster sorting in certain arrays. The in-place nature of the sorting also aids in reducing memory overhead.

In conclusion, this approach is concise, leverages modern Python capabilities, and is efficient both in terms of time and space, making it suitable for competitive programming contexts or large datasets.
```

Runtime: undefined
Memory: 19584000
"""

# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         def _count1(x:int):
#             res = 0
#             while x != 0:
#                 res += x & 1
#                 x = x >> 1
#             return res
#         representation_1s = [(_count1(x), x) for x in arr]
#         representation_1s.sort(key=lambda x: (x[0], x[1]))
#         return [x[1] for x in representation_1s]
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # bit_count() is the fastest way to count set bits in modern Python
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr
