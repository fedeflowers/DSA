"""
## Explanation of the Solution for "Finding the Number of Visible Mountains"

### 1. Brief Explanation of the Approach

The problem "Finding the Number of Visible Mountains" involves determining which mountain peaks are visible given a list of peaks defined by their position and height. The main idea is to treat each peak as an interval on the x-axis, where the left and right endpoints of this interval depend on the peak's position and height.

The solution comprises the following steps:

- **Interval Creation**: For each mountain peak represented by `(x, h)` (where `x` is the position and `h` is the height), an interval is defined as `(x - h, x + h)`. This interval marks the horizontal range where the mountain is visible.
  
- **Sorting**: The created intervals are sorted primarily by the left endpoint (`s`), and in case of a tie on the left endpoint, by the right endpoint (`e`) in descending order. This ensures that if two mountains start at the same position, the taller mountain (which ends later) is considered first.

- **Counting Visible Mountains**: The algorithm iteratively examines the sorted intervals. It keeps track of the farthest right endpoint (`max_end`) that has been confirmed visible. If a mountain's right endpoint (`e`) extends farther than `max_end`, it means this mountain is visible. Additionally, a `Counter` is used to ensure that peaks that overlap and have the same interval are only counted when they are unique.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The solution has a time complexity of `O(N log N)`, where `N` is the number of peaks. This is primarily due to the sorting step, which takes `O(N log N)` time.

- **Space Complexity**: The space complexity is `O(N)` because we store the intervals in a list and also use a `Counter` to track the frequencies of the intervals, both of which require linear space relative to the number of peaks.

### 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Showing All Intervals**: By converting peak properties into start-end intervals, the problem is transformed into a well-known problem of managing intervals rather than handling geometric properties directly.

- **Sorting Helps Manage Overlaps**: The sorting mechanism simplifies determining which peaks are visible without needing a more complex spatial data structure. After sorting, you only need to iterate through the list and maintain a simple maximum endpoint, which eliminates the need for nested loops.

- **Use of Counter for Uniqueness**: The use of `Counter` allows for efficient management of overlapping intervals, ensuring that duplicates do not inflate the count of visible mountains, optimizing the result correctly.

Overall, this approach takes advantage of sorting and linear scanning to efficiently determine visible mountains in a clear and understandable manner.

Runtime: undefined
Memory: 66328000
"""

class Solution:

    def _terminates(self, peak): #wher eth emountain ends on x axis (x1, x2)
            return (peak[0] - peak[1], peak[0] + peak[1])

    def visibleMountains(self, peaks: List[List[int]]) -> int:
        #merge intervals approach
        intervals = [self._terminates(peak) for peak in peaks]
        intervals.sort(key = lambda x: (x[0], -x[1]))
        res = 0
        max_end = -float("inf")
        c = Counter(intervals)
        for s, e in intervals:
            if e > max_end:
                if c[(s,e)] == 1:
                    res += 1
                max_end = e

        return res
