"""
```markdown
## Explanation of the LeetCode Solution for "Merge Intervals"

### 1. Brief Explanation of the Approach

The algorithm aims to merge overlapping intervals in a given list of intervals. The approach can be summarized as follows:

1. **Sorting the Intervals**: First, the `intervals` list is sorted based on the starting times of the intervals. This ensures that if two intervals overlap, they will be adjacent to each other in the sorted array.
  
2. **Merging Process**: The algorithm initializes a result list `res` with the first interval. Then, it iterates through the remaining intervals:
   - For each interval `(s, e)`, it checks the end of the last interval added to `res` (denoted as `curr_e`).
   - If `curr_e` is greater than or equal to `s`, it indicates that the current interval overlaps with the last interval in `res`. In this case, the last interval is updated by merging it with the current interval. The new end of this interval is the maximum of `curr_e` and `e`.
   - If there is no overlap, the current interval is appended to `res` as a separate interval.

3. **Return Result**: Finally, the merged intervals are returned as a list.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of the solution is O(N log N) due to the sorting step, where N is the number of intervals. The merging step is O(N) as each interval is processed once in a single pass. Therefore, the overall time complexity is O(N log N).

- **Space Complexity**: The space complexity is O(N) in the worst case, where potentially all intervals do not overlap and all intervals are stored in the result list `res`. The additional space for sorting the intervals also requires O(N) space in the average case.

### 3. Why This Approach is Efficient

This approach is efficient because:

- **Sorting Guarantees Proper Order**: By sorting the intervals first, the algorithm ensures that it only has to consider neighboring intervals to determine overlaps, reducing the potential complexity of checking all pairs of intervals.
  
- **Single Pass Merging**: The algorithm performs the merging operation in a single sweep through the intervals after sorting, making it capable of handling even large datasets efficiently.

- **Simplicity and Clarity**: The logic is straightforward, making it easy to understand and maintain. The clear separation of the sorting and merging phases helps avoid confusion, and the method uses an intuitive comparison to determine overlaps.

Overall, this method strikes a balance between computational efficiency and simplicity, making it a widely used solution for the "Merge Intervals" problem.
```

Runtime: undefined
Memory: 23412000
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        for s, e in intervals[1:]:
            curr_s, curr_e = res[-1]
            if curr_e >= s:
                res[-1] = [curr_s, max(e, curr_e)]
            else:
                res.append([s,e])

        return res
