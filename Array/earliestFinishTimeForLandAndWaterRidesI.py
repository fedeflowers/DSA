"""
```markdown
# Explanation of LeetCode Solution for "Earliest Finish Time for Land and Water Rides I"

## 1. Approach Explanation
The solution employs a two-step comparison to determine the earliest possible finish time for either land rides or water rides. The approach includes the following steps:

- **Calculate Minimum Finish Times for Rides**: It first computes the earliest finish time for all land rides and all water rides by summing the start times and durations of the rides (i.e., `start + duration`). This gives us:
  - `min_land_end`: the earliest finish time among all land rides.
  - `min_water_end`: the earliest finish time among all water rides.

- **Determine Finish Times for Different Orders**:
  - **Order 1 (Land Ride first)**: The code calculates the finishing time if the land ride that finishes first is taken before water rides. It calculates this by iterating through the water rides and finding the maximum of the earliest finish time of the land ride (`min_land_end`) and the start times of water rides. Then, it sums this with the respective durations of the water rides.
  
  - **Order 2 (Water Ride first)**: Similarly, it does the same calculation for when a water ride is taken first followed by a land ride, using the respective `min_water_end`.

- **Return the Minimum Time**: Finally, the solution returns the minimum between the two finish times calculated from the orders above (`land_then_water` and `water_then_land`).

## 2. Time and Space Complexity Analysis
- **Time Complexity**:
  - The solution performs linear passes through the lists of ride times and durations, specifically:
    - Two passes for calculating `min_land_end` and `min_water_end`.
    - Two additional passes each for calculating `land_then_water` and `water_then_land`.
  - As such, if `n` is the number of land rides and `m` is the number of water rides, the overall time complexity is O(n + m).

- **Space Complexity**:
  - The algorithm mainly uses a constant amount of extra space (for variables holding minimum times and current calculations).
  - Thus, the space complexity can be considered O(1) since it does not utilize any additional data structures that scale with input size.

## 3. Efficiency of the Approach
This approach is efficient for several reasons:
- **Linear Complexity**: Since it processes each list a limited number of times (specifically twice each), it operates in linear time relative to the size of the input, making it suitable for large inputs.
- **Direct Calculation**: By calculating minimum finish times directly and using them to evaluate only the relevant comparisons for each order, it avoids the potential inefficiencies of a more exhaustive search through all combinations of rides.
- **Simplicity of Logic**: The computational logic is clear and straightforward, making it easier to understand and maintain while still achieving optimal results. 

Overall, this efficient design allows the solution to effectively tackle the problem while maintaining manageable performance.
```

Runtime: undefined
Memory: 19548000
"""

# class Solution:
#     def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
#         mintime = float("inf")

#         for ls, ld in zip(landStartTime, landDuration):
#             for ws, wd in zip(waterStartTime, waterDuration):
#                 curr = float("inf")
#                 if ws <= ls:
#                     curr = max(ws + wd, ls) + ld
#                 elif ls <= ws:
#                     curr = max(ls + ld, ws) + wd

#                 mintime = min(mintime, curr)


#         return mintime



class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Earliest finish among all land rides (best candidate to go first).
        min_land_end = min(s + d for s, d in zip(landStartTime, landDuration))
        # Earliest finish among all water rides.
        min_water_end = min(s + d for s, d in zip(waterStartTime, waterDuration))

        # Order 1: do a land ride first (finishing at min_land_end), then a water ride.
        land_then_water = min(
            max(min_land_end, s) + d
            for s, d in zip(waterStartTime, waterDuration)
        )

        # Order 2: do a water ride first (finishing at min_water_end), then a land ride.
        water_then_land = min(
            max(min_water_end, s) + d
            for s, d in zip(landStartTime, landDuration)
        )

        return min(land_then_water, water_then_land)
