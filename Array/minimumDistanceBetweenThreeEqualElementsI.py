"""
```markdown
## Explanation of the Solution for "Minimum Distance Between Three Equal Elements I"

### 1. Brief Explanation of the Approach
This solution focuses on tracking the last two indices of each value in the array `nums`. The key observation here is that if we have three indices (let’s call them `a`, `b`, and `c`) corresponding to the same value, the formula to compute their total distance is:

\[ |a-b| + |b-c| + |c-a| = 2 \times (c - a) \]

Given that `a`, `b`, and `c` are the indices of the same value located at increasing indices (hence, `a < b < c`), the total distance simplifies to minimizing the difference between the farthest (`c`) and the nearest (`a`) index.

The process works as follows:
- Iterate over the array `nums`, keeping track of the last two indices encountered for each value in the dictionary `last_two`.
- When a value is found that appears for the third time, calculate the minimum distance as \(2 \times (i - \text{prev})\), where \(i\) is the current index and \(\text{prev}\) is the second-to-last index of that value.
- Update `last_two` to slide the window, keeping the most recent indices for future calculations.
- If at least one valid triplet is found, return the minimum distance; otherwise, return `-1`.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the list `nums`. We iterate through the list once, and each dictionary operation (insertion and lookup) is on average \(O(1)\).
  
- **Space Complexity**: \(O(m)\), where \(m\) is the number of unique values in `nums`. The dictionary `last_two` stores indices for each unique value, and in the worst case, this could be the entire list if all elements are distinct.

### 3. Why This Approach is Efficient
This approach is efficient because:
- It leverages a single pass through the input list (`nums`), meaning that no additional sorting or nested looping is needed, which would significantly increase the time complexity.
- By focusing solely on the last seen indices of each unique value, it minimizes the distance calculation directly when a third occurrence is found, thus sidestepping any need for more complex data structures or algorithms.
- The use of a dictionary allows for quick access and updates, ensuring that we can keep track of indices without overhead.

This makes the algorithm not only efficient in terms of runtime but also straightforward, adhering to clean coding principles with a clear and manageable structure.
```

Runtime: undefined
Memory: 19436000
"""

# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         # save indices, sort by vlue and index, go in 3 by 3 window and search if its good or not and save res -Z final time O(nlogn)
#         nums_index = [(v, i) for i, v in enumerate(nums)]
#         nums_index.sort(key=lambda x: (x[0], x[1]))
#         dist = float("inf")
#         #window 3 by 3 sliding
#         for i in range(len(nums_index)-2):
#             val1 = nums_index[i][0]
#             val2 = nums_index[i+1][0]
#             val3 = nums_index[i+2][0]

#             d1 = nums_index[i][1]
#             d2 = nums_index[i+1][1]
#             d3 = nums_index[i+2][1]

#             if val1 == val2 == val3:
#                 #compute distance
#                 dist = min(dist, abs(d1 - d2) + abs(d2 - d3) + abs(d3 - d1))

#         return dist if dist != float("inf") else -1


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # For sorted indices a < b < c:
        # |a-b| + |b-c| + |a-c| = 2*(c - a)
        # So just minimize (c - a), tracked via last two indices per value

        last_two: dict[int, list[int]] = {}  # val -> [prev, curr]
        dist = float("inf")

        for i, v in enumerate(nums):
            if v not in last_two:
                last_two[v] = [i]
            elif len(last_two[v]) == 1:
                last_two[v].append(i)
            else:
                prev, curr = last_two[v]
                dist = min(dist, 2 * (i - prev))
                last_two[v] = [curr, i]  # slide the window

        return dist if dist != float("inf") else -1
