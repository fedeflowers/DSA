"""
```markdown
## Explanation of the Solution for Minimize Product Sum of Two Arrays

### 1. Brief Explanation of the Approach

The problem "Minimize Product Sum of Two Arrays" involves finding two arrays such that the sum of their products is minimized. The optimal way to achieve this is by matching the smallest elements of one array with the largest elements of another array.

In this solution, we utilize the following steps:
- **Sorting**: We sort the first array (`nums1`) in ascending order and the second array (`nums2`) in descending order. This setup aligns the smallest elements of `nums1` with the largest elements of `nums2`.
- **Pairing and Summation**: We then calculate the product sum for the paired elements using a generator expression, which efficiently computes the sum of products in a single pass.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The sorting of both arrays takes O(n log n) time, where n is the length of the arrays. The subsequent summation of products takes O(n) time. Therefore, the overall time complexity is O(n log n).
  
- **Space Complexity**: The space used is O(1) beyond the input arrays (not counting input storage), as we only store some temporary variables. The sorting operation could utilize additional space in some implementations of sorting algorithms, but without persistent additional data structures in this context, we can consider the space complexity as O(1).

### 3. Why This Approach is Efficient

This approach is efficient for a few reasons:
- **Direct Pairing**: By sorting the arrays and directly pairing the largest and smallest elements, we minimize the contributions to the final sum, ensuring that larger values do not multiply with smaller counterparts, which would increase the product sum unnecessarily.
- **Simple Implementation**: The algorithm is straightforward and easy to implement, thanks to the built-in sorting functions and comprehension syntax available in Python.
- **Optimal Performance**: The O(n log n) sorting step is unavoidable for many algorithms on unsorted data, and this approach utilizes that step to produce the optimum pairing with minimal overhead and extra operations.

Overall, the combination of sorting and direct multiplicative pairing leads to a clear, fast, and effective solution for minimizing the product sum of two arrays.
```

Runtime: undefined
Memory: 22492000
"""

# class Solution:
#     def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
#         # brute force should be take min and bring it to the maximum, so maybe with two heaps is duable in n logn
#         heap1 = nums1
#         heapq.heapify(heap1) # min heap
#         heap2 = [-el for el in nums2] # max heap
#         heapq.heapify(heap2)
#         res = 0
#         while heap1 and heap2:
#             min_1 = heapq.heappop(heap1)
#             max_2 = -heapq.heappop(heap2)
#             res += min_1 * max_2

#         return res


# optimized: same O(nlogn) but faster
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        return sum(x * y for x, y in zip(nums1, nums2))
