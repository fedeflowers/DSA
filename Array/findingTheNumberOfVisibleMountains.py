"""
```markdown
## Solution Explanation for "Finding the Number of Visible Mountains"

### 1. Brief Explanation of the Approach
The objective of the problem is to determine how many mountains are visible given a list of peak coordinates represented as `[x, y]`. A mountain is defined by its x-coordinate (base center) and height (y-coordinate). 

To solve this problem, the approach involves the following steps:

1. **Transform Peaks to Intervals:** Each mountain can be represented as an interval on the x-axis defined by its left and right boundaries. For a peak at `(x, y)`, the left boundary is `x - y` and the right boundary is `x + y`. Thus, we create a list of tuples representing these intervals.

2. **Count Frequencies of Intervals:** To handle duplicate mountains (i.e., mountains with the same intervals), we utilize the `Counter` from the `collections` module to count occurrences of each interval.

3. **Sort the Intervals:** We sort the intervals primarily by their starting point in ascending order and, in cases where start points are equal, by their end point in descending order. This sorting helps in efficiently determining visibility.

4. **Count Visible Mountains:** Iterate through the sorted intervals, tracking the maximum end point encountered so far (`max_end`). If the current mountain's end extends beyond `max_end`, it means it is visible. However, we only count mountains that are unique (not duplicates) using the frequency counts from the previous step.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** 
  - Constructing the intervals from peaks takes \(O(N)\), where \(N\) is the number of peaks.
  - Counting occurrences of intervals with `Counter` also takes \(O(N)\).
  - Sorting the intervals takes \(O(N \log N)\).
  - Finally, iterating through the sorted intervals takes \(O(N)\).
  
  Overall, the time complexity is dominated by the sorting step, leading to \(O(N \log N)\).

- **Space Complexity:** 
  - Storing the intervals takes \(O(N)\).
  - The `Counter` object also takes \(O(N)\) in the worst case where all intervals are unique.

Thus, the space complexity is \(O(N)\).

### 3. Why This Approach is Efficient
This approach is efficient due to the following reasons:

- **Interval Representation:** By transforming the problem into an interval representation, we can leverage sorting and linear scans, which are standard techniques for visibility and overlap problems. Sorting allows for straightforward comparisons between mountains.
  
- **Duplicate Handling:** Using a `Counter` to track duplicate intervals prevents over-counting and accurately determines visibility.

- **Time Complexity:** The \(O(N \log N)\) time complexity is performant enough for typical constraints found in competitive programming, allowing the solution to handle larger inputs within reasonable limits.

Overall, the combination of interval representation, sorting, and careful counting results in an effective and optimal strategy for solving the problem of visible mountains.
```

Runtime: undefined
Memory: 66248000
"""

from collections import Counter
from typing import List

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # 1. Transform peaks to intervals [start, end]
        intervals = [(x - y, x + y) for x, y in peaks]
        
        # 2. Count frequencies to handle exact duplicates (both invisible)
        counts = Counter(intervals)
        
        # 3. Sort: Start Ascending, End Descending
        # Lambda logic: x[0] sorts start asc, -x[1] sorts end desc
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        visible_count = 0
        max_end = -float('inf')
        
        for start, end in intervals:
            # If current end goes beyond the max_end seen so far,
            # it is not covered by previous mountains.
            if end > max_end:
                # Only count if it's not an exact duplicate of another mountain
                if counts[(start, end)] == 1:
                    visible_count += 1
                max_end = end
                
        return visible_count
