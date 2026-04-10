"""
## Explanation of the Approach

The problem "Minimum Distance Between Three Equal Elements I" requires us to find the minimum distance between three occurrences of the same number in the list `nums`. The given solution utilizes a dictionary to keep track of the last two indices for each unique value in the list.

Here’s a step-by-step explanation of the approach:

1. **Dictionary Initialization**: We create a dictionary `last_two` where keys are the unique values in `nums` and the values are lists containing the last two indices where that value has appeared.

2. **Iterate Through the List**: We iterate through the enumerated `nums` list. For each value `v` at index `i`, we check:
   - If the value has not been seen before, we initialize its entry in the `last_two` dictionary with the current index.
   - If it has been seen once (only one index is stored), we append the current index to its list.
   - If it has been seen twice, we calculate the distance for the triplet of indices (previous indexed `prev`, current indexed `curr`, and the new index `i`). The distance is calculated using the relationship \( |a-b| + |b-c| + |a-c| = 2 \times (c - a) \) which simplifies our task significantly.

3. **Updating the Minimum Distance**: Whenever we process an occurrence of a value for the third time (and thus have three indices), we update the minimum distance if the computed distance is smaller than the previously recorded minimum.

4. **Return Value**: After processing all elements, we return the minimum distance found. If no valid triplet was found, we return -1.

## Time and Space Complexity Analysis

### Time Complexity
- The time complexity is **O(n)**, where n is the number of elements in the list `nums`. This is because we take a single pass through the list to populate `last_two` and compute distances.

### Space Complexity
- The space complexity is **O(k)**, where k is the number of unique values in `nums`. In the worst case, if all numbers are unique, this could be O(n), but typically, it is expected to be much smaller since many elements will be the same.

## Why This Approach is Efficient

1. **Minimized Operations**: Instead of sorting the array (which would typically take O(n log n)), the solution efficiently manages indices in O(n) time by only tracking the last two occurrences of each value.
  
2. **Direct Calculation of Distances**: Utilizing the relationship between absolute differences allows immediate calculation of the minimum distance when encountering a third occurrence without needing to explore every combination or subarray.
  
3. **Memory Usage**: The solution maintains a compact memory usage by strictly storing the last two indices, which is sufficient to derive the needed distances, leading to potentially less space usage compared to solutions involving combinations or full storage of triplets.

Overall, the implemented approach is efficient in both time and space, making it well-suited for large input sizes commonly encountered in competitive programming.

Runtime: N/A
Memory: N/A
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
