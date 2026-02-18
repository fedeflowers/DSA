"""
```markdown
## Explanation of the Solution for "Peak Index in a Mountain Array"

### 1. Approach Explanation
The problem "Peak Index in a Mountain Array" requires finding the index of the peak element in a given mountain array. A mountain array is defined as an array where:

- There exists an index `i` such that `arr[0] < arr[1] < ... < arr[i]` (increasing sequence) and `arr[i] > arr[i+1] > ... > arr[n-1]` (decreasing sequence).

The solution utilizes a binary search technique to efficiently find the peak index. The key steps in the algorithm are:

- Initialize two pointers, `low` and `high`, to represent the bounds of the search (starting from the beginning and end of the array).
- Use a loop to perform the binary search until `low` is less than `high`.
- Calculate the middle index `mid`.
- Compare the values at `arr[mid]` and `arr[mid + 1]`:
  - If `arr[mid] < arr[mid + 1]`, it indicates that the peak must be to the right of `mid` (or `mid` itself is not a peak), hence update `low` to `mid + 1`.
  - Otherwise, if `arr[mid] >= arr[mid + 1]`, it indicates that the peak could be at `mid` or is to the left of `mid`, hence update `high` to `mid`.
- Once the loop ends, `low` will point to the peak index, which is returned.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(log N)
  - Since the algorithm splits the search space in half with each iteration (like a binary search), it runs in logarithmic time relative to the number of elements in the array.

- **Space Complexity**: O(1)
  - The solution uses a constant amount of space for variables `low`, `high`, and `mid`, without requiring any additional data structures that grow with input size.

### 3. Efficiency of the Approach
This binary search approach is efficient for the following reasons:

- **Reduced Search Space**: By eliminating half of the elements in each iteration based on comparisons, it quickly narrows down to the peak element instead of checking each element sequentially.
- **Guaranteed Result**: Given that the problem guarantees the existence of a peak in the mountain array, the binary search leverages this property, ensuring that a peak will always be found in logarithmic time.
- **Optimal Performance**: For large arrays, the O(log N) time complexity is significantly faster compared to a linear O(N) scan, making this solution highly efficient.

Overall, the binary search method makes the solution both elegant and optimal for finding the peak index in a mountain array.
```

Runtime: undefined
Memory: 31448000
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low
            
