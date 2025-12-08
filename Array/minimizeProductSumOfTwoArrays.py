"""
```markdown
## Explanation of the Approach

The goal of the "Minimize Product Sum of Two Arrays" problem is to minimize the sum of the products of two arrays, `nums1` and `nums2`. The strategy is to match the smallest values from one array with the largest values from the other array to minimize the overall product sum.

### Steps in the Solution:

1. **Heap Creation**:
   - The first array, `nums1`, is transformed into a min-heap using `heapq.heapify()`, which allows us to efficiently get the smallest element.
   - The second array, `nums2`, is transformed into a max-heap. To do this with Python's `heapq`, which only provides a min-heap, we push the negative of each element. Thus, when we pop from this heap, we retrieve the largest element by taking the negative of the popped value.

2. **Calculating the Result**:
   - The solution iterates while both heaps are not empty. In each iteration, it pops the smallest element from `nums1` and the largest element from `nums2`, computes the product of these two, and accumulates this product into the result variable `res`.

3. **Return Result**:
   - Finally, it returns the accumulated result which represents the minimized product sum.

## Time and Space Complexity Analysis

### Time Complexity:
- The heapification of `nums1` and `nums2` takes `O(N)` time each (where N is the number of elements in the arrays).
- Popping from each heap takes `O(log N)`, and since we pop elements in a loop which iterates N times, this gives an additional `O(N log N)` component.
- **Total Time Complexity**: The overall complexity is dominated by the iterations through the heaps leading to an effective time complexity of:
  \[
  O(N \log N)
  \]

### Space Complexity:
- The space complexity is primarily O(N) since we are using heaps to store the modified elements of the input arrays.
- **Total Space Complexity**: The overall space complexity is:
  \[
  O(N)
  \]

## Why This Approach is Efficient

This approach is efficient for several reasons:

1. **Optimal Pairing**: By leveraging a min-heap for `nums1` and a max-heap for `nums2`, we ensure that in each step, the smallest element from `nums1` is paired with the largest element from `nums2`, which minimizes the product for that specific pair. This greedy strategy directly leads to minimizing the total sum.

2. **Complexity Management**: The combination of heap operations (which are `log N` efficient) and the linear nature of array processing provides a scalable solution conducive to handling large input sizes.

3. **Flexibility**: The technique can be adapted to various similar problems where you need to optimize the pairing of two lists based on some criteria.

In summary, the use of heaps not only simplifies the required operations but also allows for an efficient computation of the minimized product sum.
```

Runtime: undefined
Memory: 26100000
"""

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # brute force should be take min and bring it to the maximum, so maybe with two heaps is duable in n logn
        heap1 = nums1
        heapq.heapify(heap1) # min heap
        heap2 = [-el for el in nums2] # max heap
        heapq.heapify(heap2)
        res = 0
        print(heap1, heap2)
        while heap1 and heap2:
            min_1 = heapq.heappop(heap1)
            max_2 = -heapq.heappop(heap2)
            res += min_1 * max_2

        return res
