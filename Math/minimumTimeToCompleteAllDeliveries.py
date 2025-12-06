"""
```markdown
# Explanation of the LeetCode Solution for "Minimum Time to Complete All Deliveries"

## 1. Brief Explanation of the Approach

The solution aims to determine the minimum amount of time required for two drones to complete their respective deliveries while considering their recharging times. The approach uses a binary search technique combined with a helper function to check if a given time `t` is sufficient for the drones to complete their deliveries.

### Breakdown of the Code:

- **Input Parameters**: 
  - `d`: A list containing two integers representing the number of deliveries that Drone 1 and Drone 2 need to make.
  - `r`: A list containing two integers that represent the recharging times for Drone 1 and Drone 2 respectively.

- **Calculating LCM**:
  - The least common multiple (LCM) of the recharge times `r1` and `r2` is computed to manage the time synchronization of both drones while they are recharging.

- **is_sufficient Function**:
  - This function determines whether a given time `t` is sufficient to complete all deliveries.
  - It calculates the number of time slots available for each drone to operate based on their recharge periods.
  - It ensures that:
    - Drone 1 has enough operational slots to complete its deliveries.
    - Drone 2 has enough operational slots to complete its deliveries.
    - The combined operational slots for both drones can cover all deliveries.

- **Binary Search**:
  - A binary search is utilized to efficiently find the minimum time required.
  - The search space is defined from `1` to `(d1 + d2) * 2`, which is a safe upper bound.
  - If a midpoint time `mid` is sufficient, the search continues in the lower half. If not, it searches the upper half.

## 2. Time and Space Complexity Analysis

### Time Complexity:
- The `is_sufficient` function runs in constant time O(1) since it involves a few arithmetic operations and calculations related to the number of deliveries. 
- The binary search operates in O(log(n)), where `n` is up to `(d1 + d2) * 2`.
- Therefore, the overall time complexity of the solution is O(log(n)), where `n` is equal to the determined upper limit on time.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a fixed amount of extra space for variables and does not grow with the input size.

## 3. Why this Approach is Efficient

The use of binary search significantly optimizes the search for the minimum time by reducing the potential search space logarithmically. This makes the solution feasible even for larger values of deliveries, avoiding a direct linear or brute force check for every possible time, which could lead to inefficiencies for larger inputs. The constant time checks within the `is_sufficient` function ensure that each midpoint evaluation is quick, leading to an overall efficient solution.
```

Runtime: undefined
Memory: 17796000
"""

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        
        # Calculate LCM for the combined constraint
        lcm_r = (r1 * r2) // math.gcd(r1, r2)
        
        def is_sufficient(t):
            # Slots available for Drone 1 (not recharging at r1)
            avail_1 = t - (t // r1)
            # Slots available for Drone 2 (not recharging at r2)
            avail_2 = t - (t // r2)
            # Slots available for either (not recharging at BOTH r1 and r2)
            avail_total = t - (t // lcm_r)
            
            return (avail_1 >= d1 and 
                    avail_2 >= d2 and 
                    avail_total >= (d1 + d2))

        # Binary Search
        low = 1
        high = (d1 + d2) * 2  # Safe upper bound
        
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if is_sufficient(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
