"""
```markdown
# Explanation of the Solution for "Finding the Number of Visible Mountains"

## 1. Approach Overview

The provided solution identifies visible mountains from a list of peaks, where each peak is defined by its height (x) and radius (y). Each mountain can be represented as an interval on a number line, calculated as `[start, end]` where:
- `start = x - y` (leftmost point of the mountain),
- `end = x + y` (rightmost point of the mountain).

### Key Steps:
1. **Transform Peaks to Intervals**: Convert the list of peaks into intervals representing the range covered by each mountain.
2. **Count Duplicates**: Use a `Counter` to track the frequency of each interval to handle cases where multiple identical mountains overlap.
3. **Sort Intervals**: Sort the intervals first by their start points in ascending order, and then by their end points in descending order. This sorting ensures that when iterating through the intervals, if a mountain's end is covered by another mountain with a lower start point, it will be correctly assessed.
4. **Count Visible Mountains**: Iterate through the sorted intervals, checking whether each interval’s end goes beyond the maximum end encountered so far. If it does, it is counted as visible unless it is a duplicate mountain.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - Creating intervals: O(N), where N is the number of peaks.
  - Counting frequencies: O(N).
  - Sorting intervals: O(N log N).
  - Iterating through sorted intervals: O(N).
  
  Overall, the time complexity is dominated by the sorting step: **O(N log N)**.

- **Space Complexity**:
  - The space required for the intervals is O(N) and for the Counter is also O(N) in the worst case.
  
  Thus, the total space complexity is **O(N)**.

## 3. Efficiency of the Approach

This approach is efficient due to its combination of sorting and linear traversal, which elegantly handles the problem of overlapping mountains and duplicates. The sorting step organizes the intervals so that the check for visibility becomes straightforward and is executed in a single pass through the sorted intervals. Moreover, by leveraging a Counter, we efficiently manage duplicates without needing nested loops or complex data structures, maintaining both clarity and performance.

Overall, the algorithm's structure allows it to operate within tight time and space constraints, providing an effective solution to the problem of counting visible mountains.
```

Runtime: N/A
Memory: N/A
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
