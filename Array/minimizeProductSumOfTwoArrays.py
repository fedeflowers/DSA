"""
```markdown
# Solution Explanation for "Minimize Product Sum of Two Arrays"

## 1. Approach Overview
The problem of minimizing the product sum of two arrays can be effectively tackled using counting sort. The main idea is to make use of the constraints of the problem, specifically that the values in the input arrays are restricted within the range of [1, 100]. 

Here’s how the approach works:
- Two frequency arrays, `freq1` and `freq2`, are initialized to keep track of the occurrences of each number in `nums1` and `nums2`, respectively.
- Both arrays are filled based on the counts of the elements present in the input arrays.
- Using two pointers, `idx1` and `idx2`, we traverse the possible values. `idx1` starts from 1 (the minimum possible value) and `idx2` starts from 100 (the maximum possible value).
- At each step, we take the minimum count from both frequency arrays and compute the contribution to the product sum by multiplying the current values pointed to by `idx1` and `idx2`. These values are then multiplied by the number of pairs formed (`take`), which is the minimum of the available counts from both arrays.
- After calculating the contribution, the counts for those values are decremented, and we continue until one of the arrays runs out of values.

## 2. Time and Space Complexity Analysis
- **Time Complexity:** O(N + K)
  - Where **N** is the total number of elements in the two input arrays (sum of lengths of `nums1` and `nums2`), and **K** is the range of the numbers (which is constant, i.e., K = 100 for this problem). The operations performed during the frequency counting and the subsequent processing of the elements are linear with respect to the input size.
  
- **Space Complexity:** O(K)
  - Two frequency arrays of size 101 are used, leading to a constant space overhead. The space complexity does not depend on the input size because the maximum number of unique values is fixed at 100.

## 3. Efficiency of the Approach
This approach is efficient for several reasons:
- The counting sort strategy leverages the constraints of the input values, allowing us to effectively reduce the problem complexity compared to sorting or heap operations.
- The overall linear time complexity allows for quick execution, crucial for large input sizes.
- By effectively reducing the problem to operations on fixed-size arrays, it minimizes overhead in memory operations and execution time, making it well-suited for competitive programming scenarios or resource-limited environments.
```

Runtime: undefined
Memory: 22540000
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
# class Solution:
#     def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
#         nums1.sort()
#         nums2.sort(reverse=True)
#         return sum(x * y for x, y in zip(nums1, nums2))

# counting sort: O(n + k)
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Optimized for value range [1, 100]. Complexity: O(N + K)
        freq1 = [0] * 101
        freq2 = [0] * 101
        
        for x in nums1: freq1[x] += 1
        for x in nums2: freq2[x] += 1
        
        idx1, idx2 = 1, 100
        res = 0
        
        while idx1 <= 100 and idx2 > 0:
            if freq1[idx1] == 0:
                idx1 += 1
            elif freq2[idx2] == 0:
                idx2 -= 1
            else:
                take = min(freq1[idx1], freq2[idx2])
                res += take * idx1 * idx2
                freq1[idx1] -= take
                freq2[idx2] -= take
                
        return res
