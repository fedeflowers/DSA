"""
## Explanation of the Approach

The problem "Earliest Finish Time for Land and Water Rides I" involves determining the earliest time a ride can finish given two types of activities: land rides and water rides. The `earliestFinishTime` function calculates this time based on the start times and durations of land and water rides.

### How it Works:
1. **Initialization**: The solution starts by initializing `mintime` to infinity, which will keep track of the minimal finish time found.

2. **Nested Loops**:
   - The outer loop iterates through each land ride using its start time (`ls`) and duration (`ld`).
   - The inner loop iterates through each water ride using its start time (`ws`) and duration (`wd`).

3. **Calculating Finish Time**:
   - For each pair of land and water ride, the code checks two scenarios:
     - **Water Ride Starts Before or When Land Ride Starts**: 
       - If the water ride starts before or at the same time as the land ride, it calculates the finish time considering the water ride first:
         - `curr = max(ws + wd, ls) + ld`
     - **Land Ride Starts Before or When Water Ride Starts**:
       - If the land ride starts before or at the same time as the water ride, it calculates the finish time considering the land ride first:
         - `curr = max(ls + ld, ws) + wd`
   - In both cases, the finish time is calculated as the later of the two ride finishes (after accounting for their respective durations).

4. **Finding the Minimum Finish Time**:
   - After calculating the finish time for the current pair of rides, it updates `mintime` to hold the minimum of its current value and the calculated `curr`.

5. **Return Result**: Finally, the function returns `mintime`, which represents the earliest finish time across all combinations of land and water rides.

## Time and Space Complexity Analysis

- **Time Complexity**: The approach uses two nested loops, one iterating over land rides and another over water rides. If there are `N` land rides and `M` water rides, the time complexity is:
  \[
  O(N \times M)
  \]
  
- **Space Complexity**: The function uses a constant amount of space for variables (`mintime`, `curr`, etc.), so the space complexity is:
  \[
  O(1)
  \]

## Why This Approach is Efficient

This approach is efficient because:
1. **Direct Pairwise Comparison**: It evaluates all possible combinations of land and water rides directly through nested loops, ensuring no potential combination is missed.
2. **Simplicity**: The logic is straightforward and easy to implement, following a clear pattern for determining finish times based on starting times and durations.
3. **Optimality of Results**: Since all combinations are checked, the minimum finish time is guaranteed to be correct.

This method is particularly effective when the number of rides is relatively small, making the \(O(N \times M)\) complexity manageable.

Runtime: N/A
Memory: N/A
"""

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mintime = float("inf")

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                curr = float("inf")
                if ws <= ls:
                    curr = max(ws + wd, ls) + ld
                elif ls <= ws:
                    curr = max(ls + ld, ws) + wd

                mintime = min(mintime, curr)


        return mintime
