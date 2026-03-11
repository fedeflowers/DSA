"""
### Explanation of the Approach

The problem "Koko Eating Bananas" requires us to determine the minimum speed (bananas per hour) at which Koko can eat all the piles of bananas within a given number of hours. The solution employs a binary search strategy to efficiently find the minimum valid eating speed.

1. **Binary Search Setup**: 
   - We start with two pointers: `s` (start) initialized to 1 (the minimum possible eating speed) and `e` (end) initialized to the maximum number of bananas in any pile.
   
2. **Check Function**: 
   - The helper function `check_hours(k, piles)` calculates the total hours Koko would take to eat all the piles if she eats at speed `k`. The calculation for each pile is done by dividing the size of the pile by `k` and rounding up (using `math.ceil`) to account for any remainder bananas that would require an additional hour.

3. **Binary Search Execution**:
   - We continue the search while `s` is less than or equal to `e`. For each midpoint (`mid`) of the current range:
      - Compute how many hours it would take Koko to eat all piles at that speed using `check_hours`.
      - If the computed hours are less than or equal to `h`, it means that Koko can finish eating within the allotted time at speed `mid`, so we set `res` (result) to `mid` and continue searching for potentially smaller valid speeds by adjusting the upper bound `e`.
      - If the hours exceed `h`, we need to look for a larger eating speed by adjusting the lower bound `s`.
   
4. **Result**:
   - Once the binary search completes, `res` will contain the minimum speed required for Koko to finish all bananas within `h` hours.

### Time and Space Complexity Analysis

- **Time Complexity**: 
  - The binary search operates in `O(log(max(piles)))` since it splits the range of speeds (from 1 to the max pile size) in half each time. For each midpoint, the helper function `check_hours` operates in `O(n)`, where `n` is the number of piles we are processing. Thus, the overall time complexity becomes:
    \[
    O(n \cdot \log(\text{max(piles)}))
    \]
  
- **Space Complexity**: 
  - The space complexity is `O(1)` since we are only using a constant amount of space for variables and do not require any additional data structures like arrays or lists that scale with input size.

### Why This Approach is Efficient

- **Binary Search Utilization**: The use of binary search significantly reduces the number of speed calculations needed. Rather than checking every possible speed linearly, it narrows down the possible speeds efficiently, thus making the solution scalable even for larger inputs.
  
- **Direct Evaluation**: The `check_hours` function encapsulates the logic for evaluating how fast Koko can eat given a specific speed, allowing clear separation of concerns within the code, maintaining good readability and organization.

- **Mathematical Ceiling Function**: By using `math.ceil`, the solution effectively manages the requirement of rounding up the hours necessary to finish piles of bananas, which is crucial for ensuring accuracy in computing the total hours required. 

Overall, this combines the elegance of binary search with practical simulation of the problem scenario, making it a well-suited solution for the given constraints of the problem.

Runtime: undefined
Memory: 20588000
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return math.ceil(sum(piles) / h) #this would be correct if we had this exact number in all piles, but she can eat one pile at time
        s = 1
        e = max(piles)
        #how many hourse she takes to eat all piles?
        # if answer == h : return k
        def check_hours(k, piles):
            #k>=1
            h = 0
            for pile in piles:
                h+=math.ceil(pile/k)

            return h

        res = e #max speed
        while s <= e:
            mid = (s + e) // 2
            used_h = check_hours(mid, piles)
            if used_h <= h:
                res = mid
                e = mid -1
            else:
                s = mid +1
               
        return res


