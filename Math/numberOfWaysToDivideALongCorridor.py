"""
```markdown
## Explanation of the Solution for "Number of Ways to Divide a Long Corridor"

### 1. Brief Explanation of the Approach
This solution aims to find the number of ways to divide a corridor filled with seats ('S') into pairs. The corridor is represented as a string, and the goal is to ensure that every pair of seats is separated by at least one empty section. Here is a breakdown of the process:

- **Step 1**: Indices of all seats are collected in a list called `seats`.
- **Step 2**: The function checks if the number of seats is even and greater than zero. If not, it returns 0 as it is not possible to form pairs.
- **Step 3**: The program iterates through the indices of the seats in steps of two (to access the pairs). For each pair, it calculates the gaps between the end of one pair and the start of the next pair. The product of these gaps gives the total number of ways to place the pairs of seats while ensuring they are separated, and is done modulo \(10^9 + 7\).

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The time complexity of the algorithm is O(N), where N is the length of the input string `corridor`. This is because we traverse the corridor once to collect seat indices and again to calculate the product of gaps.
  
- **Space Complexity**: 
  - The space complexity is O(M), where M is the number of 'S' characters found in the corridor. This is the space required to store the indices of the 'S' characters in a list.

### 3. Why This Approach is Efficient
This approach is efficient because:
- It only loops through the string a constant number of times (once to gather seat indices and once to compute gaps), ensuring linear time complexity relative to the size of the string.
- By collecting indices upfront, it avoids repeated scans of the string or complex operations, keeping constant space usage dependent only on the number of seats, rather than the total string length.
- The method carefully handles cases where the number of seats is odd or zero at the outset, reducing unnecessary computation for invalid cases.

Overall, this implementation efficiently computes the number of ways to pair the seats while maintaining separation, adhering to the defined problem constraints.
```

Runtime: undefined
Memory: 22448000
"""

# class Solution:
#     def numberOfWays(self, corridor: str) -> int:
#         MOD = 10 ** 9 + 7
#         # if number of seats is odd return 0
#         if corridor.count("S") % 2 != 0 or corridor.count("S") == 0:
#             return 0
        
#         # count the gaps + 1 between seats and multiply them for computing permutations
#         curr_s = 0
#         curr_gaps = 0
#         res = 1
#         for el in corridor:
#             if curr_s == 2:
#                 curr_gaps += 1
#             if el == 'S':
#                 if curr_s == 2:
#                     res *= curr_gaps
#                     curr_gaps = 0
#                     curr_s = 0
#                 curr_s += 1

#         return res%MOD

#BETTER WRITING

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # 1. Collect indices of all seats
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        # 2. Check validity: Must have seats and total count must be even
        if not seats or len(seats) % 2 != 0:
            return 0
        
        # 3. Calculate product of gaps between pairs
        # We look at the gap between the end of one pair (index 1, 3...) 
        # and start of next (index 2, 4...)
        res, mod = 1, 10**9 + 7
        for i in range(2, len(seats), 2):
            # (Start of Pair 2) - (End of Pair 1) gives valid positions
            res = (res * (seats[i] - seats[i-1])) % mod
            
        return res
