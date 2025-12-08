"""
```markdown
# Explanation of the LeetCode Solution for "Minimize Product Sum of Two Arrays"

## 1. Brief Explanation of the Approach

The problem requires us to minimize the product sum of two arrays, `nums1` and `nums2`. To achieve this, the optimal strategy is to pair the smallest elements of the first array with the largest elements of the second array. This way, it minimizes the contribution of higher values in the product sum, as large values in one array will counterbalance smaller values in the other.

The solution utilizes heaps (priority queues) to efficiently retrieve the smallest and largest elements from the two arrays:
- It first converts `nums1` into a min-heap (to easily access the smallest element).
- It transforms `nums2` into a max-heap by negating its elements (since Python only has a min-heap natively). This allows easy access to the largest elements.
- The algorithm then pops the smallest element from `nums1` and the largest element from `nums2` repeatedly, multiplying them together and adding the result to a running total (`res`).

Finally, the accumulated sum `res` is returned as the result.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is O(N log N), where N is the number of elements in the arrays. This complexity arises from:
  - Heapifying both arrays, which each takes O(N).
  - The while loop runs N times, and each pop operation from a heap takes O(log N).

- **Space Complexity**: The space complexity is O(N) due to the storage required for the heaps. Two additional arrays are created to heapify `nums1` and `nums2`, leading to this space usage.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:
- **Optimal Pairing**: By directly using heaps to access the smallest and largest elements, the algorithm ensures that each pairing is optimal for minimizing the product sum.
- **Reduced Complexity**: The use of heaps reduces the need for additional sorting (O(N log N) as opposed to O(N log N) for sorting, which is already utilized in heapification).
- **Iterative Calculation**: The direct multiplication and accumulation of the product sum during the while loop minimizes the number of operations and also maintains clarity in the logic, avoiding unnecessary intermediate storage or calculations.

Overall, this method balances efficiency and simplicity, making it a suitable solution for the problem.

```

Runtime: undefined
Memory: 25968000
"""

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # brute force should be take min and bring it to the maximum, so maybe with two heaps is duable in n logn
        heap1 = nums1
        heapq.heapify(heap1) # min heap
        heap2 = [-el for el in nums2] # max heap
        heapq.heapify(heap2)
        res = 0
        while heap1 and heap2:
            min_1 = heapq.heappop(heap1)
            max_2 = -heapq.heappop(heap2)
            res += min_1 * max_2

        return res
