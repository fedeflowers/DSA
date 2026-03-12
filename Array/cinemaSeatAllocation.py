"""
## Cinema Seat Allocation Solution Explanation

### 1. Approach

The problem is to maximize the number of families that can be seated in a cinema given certain reserved seats. In each row of the cinema, only specific groups of four adjacent seats can accommodate families. The solution utilizes bit manipulation to represent the occupied seats in each row, effectively allowing the algorithm to quickly check the availability of seats for potential families.

#### Steps:
- **Initialization**: Create a bitmask representation for reserved seats using a dictionary called `occupied`. Each row's occupied seats are represented by an integer (bitmask) where each bit corresponds to a seat (1 for reserved, 0 for available).
- **Initial Count**: Estimate the maximum possible families by assuming that every row without reserved seats can accommodate 2 families (as there are three possible seat configurations).
- **Check Occupied Rows**: For each row, check against the bitmasks for three possible configurations to seat families:
  - The left block (seats 2-5)
  - The right block (seats 6-9)
  - The middle block (seats 4-7)
- **Configuration Validation**: For each row, determine how many families can fit based on the reserved seats:
  - If both left and right blocks are free, count 2 families.
  - Otherwise, if at least one of the three blocks is free, count 1 family.
- **Final Calculation**: Accumulate the counts for all rows to get the total number of families that can be seated.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The space used by `occupied` is proportional to the number of rows `n`, thus iterating over the reserved seats (O(m)) and checking configurations (O(1) for each row of bitmask checks), results in a total time complexity of O(n + m), where m is the number of reserved seats.
  
- **Space Complexity**: 
  - The solution uses a dictionary to store the bitmask of occupied seats for each row, which in the worst case can create `n` entries. Thus, the space complexity is O(n).

### 3. Efficiency of the Approach

This approach is efficient because:
- **Bit Manipulation**: Using bit masks allows for rapid checks of seat availability with simple bitwise operations, avoiding the overhead associated with more verbose data structures like lists or arrays for individual seat status.
- **Direct Computation**: By directly calculating the maximum possible families based on configurations at each iteration, the algorithm minimizes unnecessary checks, leading to quick computing without exhaustive checking of every possible arrangement.
- **Utilization of Reserved Data**: Instead of creating a full seat layout, the method cleverly utilizes the reserved seat data to build only the necessary state, ensuring we handle large inputs gracefully without excessive memory use.

In summary, this solution efficiently allocates seats by leveraging bit manipulation techniques to ensure swift checks and computations within the constraints defined by reserved seating, leading to optimal performance in both time and space.


Runtime: undefined
Memory: 22816000
"""

# class Solution:
#     def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
#         # a group of 4 can be placed only in 3 positions in a row, check if those are free and that put 2 groups if you can otherwise 1 if you can (only central)
#         seats = [10 * [0] for _ in range(n)]
#         #add seats
#         for x,y in reservedSeats:
#             seats[x-1][y-1] = 1

#         groups = 0

#         for rows in seats:
#             first_grp = rows[1] == 0 and rows[2] == 0 and rows[3] == 0 and rows[4] == 0
#             second_grp = rows[5] == 0 and rows[6] == 0 and rows[7] == 0 and rows[8] == 0
#             trd_grp = rows[3] == 0 and rows[4] == 0 and rows[5] == 0 and rows[6] == 0

#             if first_grp and second_grp :
#                 groups += 2
#             elif first_grp or second_grp or trd_grp:
#                 groups += 1

#         return groups

            
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map row index to a bitmask of reserved seats
        occupied = defaultdict(int)
        for r, c in reservedSeats:
            occupied[r] |= (1 << (c - 1))
        
        # Start by assuming all rows can take 2 families
        res = (n - len(occupied)) * 2
        
        # Bitmasks for the three possible 4-seat blocks
        # Positions: [2,3,4,5], [6,7,8,9], [4,5,6,7]
        left_block = 0b0111100000  # Seats 2-5
        right_block = 0b0000011110 # Seats 6-9
        mid_block = 0b0001111000   # Seats 4-7
        
        for mask in occupied.values():
            found_two = False
            count = 0
            
            # Check if left and right blocks are both free
            if not (mask & left_block) and not (mask & right_block):
                count = 2
            # Otherwise check if at least one of the three blocks is free
            elif not (mask & left_block) or not (mask & right_block) or not (mask & mid_block):
                count = 1
                
            res += count
            
        return res

