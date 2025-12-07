"""
```markdown
## Solution Explanation for "Minimum Time to Complete All Deliveries"

### 1. Approach Explanation

The problem requires finding the minimum time necessary for a drone to complete a certain number of deliveries, taking into account that the drone has two different resting times for two sets of deliveries.

The solution uses a binary search approach combined with a helper function `enough_time` which checks if the drone can complete the required deliveries within a given time:

- **LCM Calculation**: First, the least common multiple (LCM) of the two resting periods, `r1` and `r2`, is calculated. This LCM helps determine how many complete cycles of both resting schedules fit into the given time.
  
- **Chores Calculation**: The helper function calculates:
  - `chores_1`: The total number of deliveries the drone can complete for the first set (based on `r1`) within the specified time.
  - `chores_2`: The total number of deliveries it can complete for the second set (based on `r2`).
  - `common_chores`: The total number of deliveries it can complete for the tasks that require both resting times (e.g., when both deliveries are factored in).
  
- **Conditions Check**: The function then checks if:
  - The chores completed for set 1 (`chores_1`) are at least equal to the required deliveries (`d1`).
  - The chores for set 2 (`chores_2`) are at least `d2`.
  - The common chores calculated are at least the sum of both required deliveries (`d1 + d2`).
  
- **Binary Search**: In the `minimumTime` function, binary search is used to find the minimum time required to satisfy the conditions: 
  - `low` represents the lowest possible time (starting with 0).
  - `high` is set to a maximum possible time based on the sum of deliveries multiplied by the greater resting period, ensuring enough leeway to cover maximum delivery times.
  
  During each iteration, the mid-point is calculated, and the `enough_time` function is called to verify if the current mid-point time can satisfy the delivery requirements. If it can, the result is updated, and the search continues for potentially smaller times; if not, the search continues in higher time frames.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The binary search runs in **O(log(max_time))**, where `max_time` is equivalent to `(d1 + d2) * max(r1, r2) * 2`. In each iteration of the binary search, the `enough_time` function is called, which itself performs a constant amount of work (calculating some basic arithmetic and the gcd of two numbers). Thus, the overall time complexity is **O(log(max_time))**.

- **Space Complexity**: 
  - The space complexity is **O(1)**, as the algorithm only uses a fixed amount of extra space (for variables) regardless of the input size.

### 3. Why This Approach is Efficient

This approach is efficient for the following reasons:

- **Binary Search**: By using binary search to find the minimum time, the algorithm operates logarithmically with respect to the possible maximum time, making it significantly faster than a linear search or brute force approach, especially as the number of deliveries increases.

- **Mathematical Optimization**: The calculation of LCM and the arithmetic operations in the `enough_time` function allow for efficient checks of whether the drone can complete the necessary deliveries without simulating each possible delivery in detail.

- **Early Stopping**: The checks are designed to quickly eliminate impossible timeframes, thus rapidly narrowing down the search space.

Overall, this combination allows the solution to efficiently reach the correct answer in a reasonable time.
```

Runtime: undefined
Memory: 17648000
"""

class Solution:
    def enough_time(self, time: int, r1: int, r2: int, d1: int, d2: int) -> bool:
        lcm = (r1 * r2 ) // math.gcd(r1,r2) # to understand common resting times
        chores_1 = time - (time // r1) # the drone can make these deliveries
        chores_2 = time - (time // r2)
        common_chores = time - (time // lcm)

        return chores_1 >= d1 and chores_2 >= d2 and common_chores >= (d1+d2)

    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1,d2 = d
        r1,r2 = r
        low = 0
        high = (d1 + d2) * max(r1, r2) * 2
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.enough_time(mid, r1, r2, d1, d2):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res        
