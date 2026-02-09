"""
```markdown
# Explanation of the Hit Counter Solution

## 1. Approach

The provided solution implements a simple hit counter that tracks the number of hits over a rolling 5-minute (300 seconds) window. The `HitCounter` class has two main attributes: `times` and `hits`, both of which are fixed-size lists with a length of 300.

- **Initialization**: 
  - `self.times` keeps track of the timestamps (in seconds) when hits occurred for each of the last 300 seconds.
  - `self.hits` counts how many hits occurred at each corresponding second in `self.times`.

- **hit() Method**: 
  - When a hit is recorded by calling the `hit(timestamp)` method, the index (`idx`) is calculated using the modulus operator (`timestamp % 300`), which ensures that it wraps around the 300-second window.
  - If the timestamp at that index (`self.times[idx]`) does not match the current timestamp, it means that this slot is for a new second. In this case, it updates the timestamp and resets the count of hits to 1.
  - If the timestamp matches, it simply increases the count of hits for that second.

- **getHits() Method**: 
  - This method calculates the total number of hits in the last 300 seconds from the given `timestamp`.
  - It iterates through the `times` array and sums up the hits for each second that falls within the 300-second window relative to the `timestamp`.

## 2. Time and Space Complexity Analysis

- **Time Complexity**:
  - The `hit(timestamp)` method runs in O(1) time since it performs constant-time operations to update the counts.
  - The `getHits(timestamp)` method runs in O(300) = O(1) time (since it always loops through a fixed size of 300). 

- **Space Complexity**:
  - The space complexity is O(1) since the size of the `times` and `hits` lists is fixed (300 elements each).

## 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Fixed Size**: By using fixed-size arrays (300 slots), the solution guarantees that it uses a constant amount of space, which is optimal for this problem that deals with a rolling time window.
- **Constant Time Operations**: Both the hit and get hits operations are efficiently constant time, making them suitable for real-time applications where performance is critical.
- **Handles Overflow**: Using the modulus operation allows the algorithm to gracefully handle the wrapping of timestamps and ensures that it always deals with the latest 300 seconds of data.
- **Logical Separation**: The design clearly separates responsibilities, with one method for logging hits and another for retrieving counts, enhancing modularity and readability of the code.

Overall, this is an effective solution for the "Design Hit Counter" problem that maintains performance and simplicity.
```

Runtime: N/A
Memory: N/A
"""

class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total
