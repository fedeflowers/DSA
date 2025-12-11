"""
## Explanation of the Solution for "Count Covered Buildings"

### 1. Brief Explanation of the Approach

The solution approaches the problem by grouping the building coordinates primarily by their x-coordinates and then by their y-coordinates. Here's a step-by-step breakdown of the approach:

- **Grouping Coordinates:** Two default dictionaries (`group_x` and `group_y`) are created. `group_x` maps x-coordinates to a list of corresponding y-coordinates, while `group_y` does the opposite, mapping y-coordinates to x-coordinates.

- **Sorting:** Each list in both `group_x` and `group_y` is sorted. This allows for easy comparison of y-values for a particular x-coordinate and x-values for a particular y-coordinate when checking for coverage.

- **Counting Covered Buildings:** The solution iterates over each building defined by its coordinates (x, y) and checks if it is covered by other buildings:
  - A building is considered "covered" if:
    - The smallest y-value associated with its x-coordinate is not `y` (i.e., there exists another building with the same x-coordinate but a different y-coordinate).
    - The largest y-value associated with its x-coordinate is not `y`.
    - Similarly, for the y-coordinate, it checks if the smallest and largest x-values do not equal `x`.
  
- If all four conditions hold true for a building, it is counted as a "covered" building.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** 
  - The solution involves iterating over the list of buildings twice: once to group coordinates and once to check coverage. 
  - Each grouping operation takes O(m log m) due to sorting, where `m` is the maximum number of y-coordinates for any x and also the maximum number of x-coordinates for any y.
  - Thus, if there are `n` buildings, the overall time complexity can be expressed as O(n log n) due to the sorts, making it O(n log n) as a dominant factor.

- **Space Complexity:** 
  - The solution uses extra space to maintain two dictionaries (`group_x` and `group_y`). In the worst case, the total space required is O(n), where all buildings have distinct coordinates.

### 3. Why This Approach is Efficient

- **Coordinate Grouping:** By organizing buildings based on their x and y coordinates, the method efficiently reduces the complexity of checking for coverage. Instead of individually checking each building against every other building, it leverages sorted lists for quick comparison.

- **Early Stopping:** The checks for coverage are optimized by confirming if the first and last y-values or x-values are equal, thus providing a quick way to decide coverage without needing to examine all coordinates.

- **Sorting:** Sorting facilitates efficient searching for minimum and maximum values, making the counting of covered buildings straightforward with minimal overhead.

This approach strikes a balance between clarity and efficiency, making it suitable for larger lists of buildings while maintaining the necessary correctness through structured grouping and verification.

Runtime: undefined
Memory: 60012000
"""

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        #group by coordinate
        group_x = defaultdict(list)
        group_y = defaultdict(list)
        for x,y in buildings:
            group_x[x].append(y)
            group_y[y].append(x)

        for k in group_x:
            group_x[k].sort()
        
        for k in group_y:
            group_y[k].sort()

        res = 0
        for x, y in buildings:
            if (
                group_x[x][0] != y
                and 
                group_x[x][-1] != y 
                and
                group_y[y][0] != x
                and
                group_y[y][-1] != x
                ):
                res += 1

        return res
