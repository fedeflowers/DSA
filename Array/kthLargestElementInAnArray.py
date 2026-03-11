"""
```markdown
# Explanation of the LeetCode Solution for "Kth Largest Element in an Array"

## 1. Brief Explanation of the Approach

The provided solution aims to find the Kth largest element in a list of integers, `nums`. The approach follows these steps:

1. **Sorting**: The input list `nums` is sorted in ascending order using the built-in `sort()` method.
2. **Accessing the Kth Largest Element**: Once sorted, the Kth largest element can be accessed by indexing into the sorted list. Specifically, the Kth largest element is located at the index `len(nums) - k`. This is because the largest element is at the last index (len(nums) - 1) and going backwards will yield the correctly indexed Kth largest element.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this approach is dominated by the sorting operation, which is \(O(N \log N)\), where \(N\) is the number of elements in the input list `nums`. The subsequent access to the Kth largest value is \(O(1)\).

- **Space Complexity**: The space complexity is \(O(1)\) if we do not account for the space used by the sorting algorithm. However, because Python's `sort()` function might use additional space for managing the sorting process, the effective space complexity can be considered \(O(N)\) in a worst-case scenario for the sorting operation (not including the input array itself).

## 3. Why This Approach is Efficient

This approach is effective for a few reasons:

1. **Simplicity**: The solution is concise and straightforward, making it easy to understand and implement. Sorting is a well-known operation that allows for easy access to ordered elements.
2. **Direct Access**: By sorting the array first, we can directly access the Kth largest element with a simple index calculation, which avoids more complex logic or data structures.
3. **Sufficient for Smaller Inputs**: For smaller input sizes, the sorting method performs adequately since \(O(N \log N)\) is computationally feasible. This method can become less efficient when dealing with very large datasets or when performance is critical.
   
However, it's essential to note that while this approach is straightforward and works within the problem's constraints, there are more efficient algorithms (like Quickselect) that can solve the problem in average \(O(N)\) time.
```


Runtime: undefined
Memory: 30836000
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
