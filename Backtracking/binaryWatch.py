"""
```markdown
## Explanation of the Solution for "Binary Watch"

### 1. Brief Explanation of the Approach
The problem requires generating all valid times that can be displayed on a binary watch based on a specified number of LEDs that are turned on. A binary watch has 12 hours and 60 minutes; thus, we need to consider combinations of these hour and minute values that yield a specific count of turned-on LEDs.

The solution uses the following steps:
- **Helper Function:** A helper function `_bitcount(x)` calculates the number of '1's in the binary representation of an integer `x`, essentially counting how many LEDs are on.
- **Validation:** It first checks whether the number of LEDs turned on (`turnedOn`) is within valid bounds (0-8). If not, it returns an empty list immediately.
- **Nested Loop:** The solution iterates through all possible hours (0 to 11) and minutes (0 to 59):
  - For each hour and minute combination, it computes the total number of LEDs turned on by combining the count from `_bitcount(h)` for the hour and `_bitcount(m)` for the minute.
  - If the total matches `turnedOn`, it formats the time string in HH:MM format, ensuring that minutes are displayed as two digits (using `m:02d`) and adds it to the results list.
- **Return Result:** Finally, it returns the list of valid time strings.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** The time complexity is O(12 * 60), which simplifies to O(1) since the limits for hours and minutes are constants. Thus, the algorithm iterates through a fixed number of combinations regardless of input size.
  
- **Space Complexity:** The space complexity is O(1) for variables since the only list created to store the results depends on the valid combinations, which is also limited. In the worst case, if all combinations with the specified `turnedOn` are valid, the output list can hold at most 12 entries.

### 3. Why This Approach is Efficient
This approach efficiently enumerates all possible times without any complex data structures or algorithms since the range of valid hour and minute combinations is limited and well-defined. The use of a nested loop, combined with a simple counting operation, ensures that all valid combinations are checked within a constant time frame. Given the constraints of the problem, this brute-force approach is manageable and effective, yielding results without unnecessary overhead.
```

Runtime: undefined
Memory: 19344000
"""

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def _bitcount(x):
            return bin(x).count('1')


        if turnedOn <0 or turnedOn > 8:
            return []

        result = []

        for h in range(12):
            for m in range(60):
                total_on = _bitcount(h) + _bitcount(m)
                if total_on == turnedOn:
                    res = f'{h}:{m:02d}'
                    result.append(res)

        return result
