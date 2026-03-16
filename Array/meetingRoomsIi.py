"""
## Solution Explanation for "Meeting Rooms II"

The problem "Meeting Rooms II" requires us to determine the minimum number of meeting rooms required to accommodate all meetings given their start and end times. The solution provided uses a two-pointer technique to efficiently calculate the overlapping intervals.

### 1. Approach Explanation

The solution can be broken down into the following steps:

- **Extract and Sort Start and End Times:** 
  - It creates two separate lists: one for the start times and one for the end times of the meetings. Both lists are then sorted. Sorting is essential as it allows us to process the meeting times in chronological order.
  
- **Two-Pointer Technique:** 
  - We use two pointers: `s` for the start times and `e` for the end times.
  - We initialize `rooms` and `max_rooms` to keep track of the current number of rooms in use and the maximum number of rooms needed at any point, respectively.
  - We iterate using the pointers:
    - If the next meeting starts before the earliest ending meeting finishes (`starts[s] < ends[e]`), we need to allocate a new room. Therefore, we increase the `rooms` count and move the start pointer `s` forward.
    - If the next meeting starts after or when the earliest meeting ends (`starts[s] >= ends[e]`), we can free up a room, so we decrease the `rooms` count and move the end pointer `e` forward.
  - During each iteration, we check and update the maximum rooms needed (`max_rooms`).

- **Return Result:** 
  - After processing all meetings, the value of `max_rooms` will represent the minimum number of meeting rooms required.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** 
  - The most time-consuming operations are sorting the start and end times. Sorting each list takes \(O(N \log N)\), where \(N\) is the number of meetings (intervals). The subsequent linear iteration through the lists takes \(O(N)\). Thus, the overall time complexity is:
    \[
    O(N \log N)
    \]

- **Space Complexity:**
  - We are using additional space for the two separate lists (start times and end times). Each of these lists requires \(O(N)\) space, hence the total space complexity is:
    \[
    O(N)
    \]

### 3. Why This Approach is Efficient

This approach is efficient due to the following reasons:

- **Optimal Time Usage:** Sorting the times allows us to effectively manage overlapping with a single pass through the already sorted data, which is significantly more efficient compared to a nested loop approach that might check every interval against every other interval.
- **Simplicity:** The two-pointer technique cleanly handles room allocation for meetings without the need for complex data structures.
- **Clarity of Logic:** The separation of start and end times allows clear reasoning about when to allocate or free up rooms, making the code easier to understand and maintain.

Overall, this solution strikes a good balance between simplicity and performance, making it well-suited for handling the problem at scale.

Runtime: undefined
Memory: 21548000
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        rooms = max_rooms = 0
        s = e = 0
        
        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)
            
        return max_rooms
