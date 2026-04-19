"""
```markdown
### Explanation of the Solution for "Maximum Distance Between a Pair of Values"

1. **Approach Explanation:**
   The problem requires finding the maximum distance between pairs of values from two lists, `nums1` and `nums2`, such that the value from `nums1` is less than or equal to the value from `nums2`. The distance is defined as the difference in their respective indices.

   The solution employs a binary search strategy to efficiently find a valid index in `nums1` for each value in `nums2`. The approach involves the following steps:
   - For each element `nums2[j]`, determine the index `i` in `nums1` such that `nums1[i]` is the largest value less than or equal to `nums2[j]`.
   - The binary search function (`bin_search`) scans through `nums1` up to the index `j` (or the last index of `nums1`, whichever is smaller) to find `i`.
   - For every valid index `i`, calculate the distance `j - i` and update the maximum found distance.

2. **Time and Space Complexity Analysis:**
   - **Time Complexity:** `O(N log M)`
     Where `N` is the length of `nums2` and `M` is the length of `nums1`. Each iteration over `nums2` (of length `N`) involves a binary search over `nums1` (up to length `M`), which takes `O(log M)`.
   - **Space Complexity:** `O(1)`
     The solution uses constant extra space, as it only employs a few integer variables and does not allocate any additional data structures that grow with input size.

3. **Efficiency of the Approach:**
   This approach is efficient because:
   - It leverages binary search, reducing the overall number of comparisons and thus significantly speeding up the solution compared to a brute-force O(N * M) method where every pair is compared.
   - The constraints of non-decreasing sequences in binary search ensure that we can quickly locate the appropriate index in `nums1` that meets the condition without scanning every element sequentially.
   - The consideration of boundaries (`right_bound = min(j, len(nums1) - 1)`) ensures that the binary search is always conducted within valid index limits of `nums1`, preventing unnecessary checks and enhancing performance.

Overall, this solution efficiently combines binary search with an iterative approach to achieve the desired result while maintaining optimal resource usage.
```

Runtime: undefined
Memory: 36068000
"""

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def bin_search(right_bound, target):
            # find leftmost i in [0, right_bound] with nums1[i] <= target
            # arrays are non-increasing, so nums1[i] <= target is a suffix
            left, right = 0, right_bound
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums1[mid] <= target:
                    res = mid
                    right = mid - 1  # try to go further left
                else:
                    left = mid + 1
            return res

        best = 0
        for j in range(len(nums2)):
            right_bound = min(j, len(nums1) - 1)
            i = bin_search(right_bound, nums2[j])
            if i != -1:
                best = max(best, j - i)
        return best
