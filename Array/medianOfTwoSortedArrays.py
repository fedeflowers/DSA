"""
## Explanation of the Solution for "Median of Two Sorted Arrays"

### 1. Approach Explanation

The provided solution uses a binary search technique to efficiently find the median of two sorted arrays, `nums1` and `nums2`. The key points of this approach are:

- **Initial Setup**: The algorithm ensures that `nums1` is always the smaller of the two arrays. This helps simplify the binary search as we limit our search space. 

- **Binary Search**: The search is conducted on the smaller array (`nums1`). The key variables include:
  - `i`: The partition index in `nums1`
  - `j`: The corresponding partition index in `nums2` calculated as `(m + n + 1) // 2 - i`, where `m` and `n` are the lengths of `nums1` and `nums2`, respectively.

- **Partition Validity**: The algorithm checks whether the current partitions satisfy the properties of valid partitions:
  - `maxLeft1 <= minRight2` (ensures all elements in the left partition of `nums1` are less than or equal to all elements in the right partition of `nums2`)
  - `maxLeft2 <= minRight1` (ensures all elements in the left partition of `nums2` are less than or equal to all elements in the right partition of `nums1`)

- **Median Calculation**:
  - If the combined length of the two arrays (`m + n`) is odd, the median is the maximum of the left partitions.
  - If it is even, the median is the average of the maximums of the left partitions and the minimums of the right partitions.

- **Adjustments**: If the partitions are not valid, the algorithm adjusts the binary search pointers (`left` and `right`) to continue the search until valid partitions are found.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The solution operates in O(log(min(m, n))) time. This is because it performs a binary search on the smaller array, ensuring that in the worst-case scenario, the number of operations is logarithmic relative to the size of the smaller array.

- **Space Complexity**: The space complexity is O(1). The algorithm uses a constant amount of space for variables and does not utilize any additional data structures that scale with input size.

### 3. Efficiency of this Approach

This approach is considered efficient for several reasons:

- **Binary Search Utilization**: By leveraging binary search on the smaller array, the algorithm avoids a linear scan through both arrays, which would take O(m+n) time.

- **Handling Different Lengths**: The solution gracefully handles cases where the two arrays are of different lengths by always working on the smaller one, simplifying the logic.

- **Direct Median Calculation**: Instead of merging the arrays (which can be an expensive operation), it directly calculates the median based on the properties of sorted arrays, leading to a very efficient solution.

Overall, this approach combines binary search with a deep understanding of the properties of medians and sorted arrays to yield an optimal and elegant solution.

Runtime: undefined
Memory: 19480000
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            maxLeft1 = nums1[i-1] if i > 0 else float('-inf')
            minRight1 = nums1[i] if i < m else float('inf')
            maxLeft2 = nums2[j-1] if j > 0 else float('-inf')
            minRight2 = nums2[j] if j < n else float('inf')
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1
