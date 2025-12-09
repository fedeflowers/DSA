"""
## Explanation of the Approach

The problem "Set Intersection Size At Least Two" requires us to determine the minimum size of a set \( S \) such that each interval in a given list of intervals contains at least two elements from \( S \). 

The solution employs the following approach:

1. **Sorting the Intervals**: The intervals are first sorted primarily by their end times (`x[1]`) in ascending order, and secondarily by their start times (`-x[0]`) in descending order. This sorting helps in managing overlap and ensuring that while we cover multiple intervals, we effectively minimize the size of the set \( S \).

2. **Initializing the Set**: An empty list `pre` is used to keep track of the last elements included in the set \( S \). The variable `ans` keeps count of the total elements added to \( S \).

3. **Iterating through Intervals**: The algorithm then iterates through the sorted intervals:
   - If `pre` is empty or the last added element (stored in `pre[1]`) is less than the start of the current interval (`s`), it means that the previous elements cannot satisfy the current interval. Therefore, we add two new elements (the end of the current interval minus one and the end of the current interval itself) to \( S \), incrementing `ans` by 2.
   - If the previous elements can cover the current interval (i.e., `pre[0] < s`), it indicates that at least one of the previous elements can fulfill the current interval's requirement. Hence, we only add one new element (the end of the current interval) to \( S \), incrementing `ans` by 1.

4. **Return the Result**: Finally, the total elements counted in `ans` represents the minimum size of the set \( S \).

## Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of the solution is \( O(N \log N) \), where \( N \) is the number of intervals. This is primarily due to the sorting step. The subsequent iteration through the intervals runs in \( O(N) \).

- **Space Complexity**: The space complexity is \( O(1) \) aside from the input space since we use a fixed amount of extra space for variables (`ans` and `pre`).

## Why This Approach is Efficient

The sorting technique effectively bundles overlapping intervals together, allowing for a greedy choice that ensures the minimum elements are selected:

1. By sorting the intervals, the algorithm maximizes its coverage of multiple intervals with the fewest new elements.
2. The greedy strategy of adding elements to \( S \) only when necessary minimizes the additional elements needed, thus ensuring efficiency.
3. The method of carefully selecting two elements or one element based on the overlap condition reduces unnecessary additions to \( S \) while fulfilling the core requirement of at least two distinct elements for each interval.

Overall, this approach is efficient in terms of both time and space, making it suitable for this problem.

Runtime: undefined
Memory: 19380000
"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end-time ascending (x[1])
        # THEN by start-time descending (-x[0])
        intervals.sort(key = lambda x: (x[1], -x[0])) 
        
        ans = 0
        pre = []
        
        for (s, t) in intervals:
            if not pre or pre[1] < s:
                ans += 2
                pre = [t-1, t]
            elif pre[0] < s:
                ans += 1
                pre = [pre[1], t]
                
        return ans
