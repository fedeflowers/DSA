"""
## Explanation of the "Fruit Into Baskets" Solution

### 1. Brief Explanation of the Approach
The solution employs the sliding window technique to solve the "Fruit Into Baskets" problem, which requires identifying the maximum number of fruits (represented by integers) that can be collected from a linear array, adhering to the constraint of only allowing two distinct types of fruits at any time.

- **Initialization**: A dictionary (`window_els`) is used to keep track of the count of each type of fruit in the current window, and two pointers (`s` for the start and `e` for the end) define the current window.
  
- **Expanding the Window**: The algorithm iterates over each element in the `fruits` list. For each fruit at index `e`, it is added to the dictionary and its count is incremented.

- **Contracting the Window**: If the number of distinct fruit types exceeds two (i.e., `len(window_els) > 2`), the starting pointer `s` is incremented to reduce the size of the window until there are at most two distinct types of fruits. The count of the fruit at the `s` pointer is decremented and removed from the dictionary when its count reaches zero.

- **Updating Maximum Length**: During each iteration, the length of the current valid window (number of fruits between the pointers `s` and `e`) is calculated, and the maximum length found so far is updated using `w_l`.

Finally, the maximum length (`w_l`) is returned, which represents the largest number of fruits that can be collected under the given constraints.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N) - The algorithm iterates through the `fruits` array once with a sliding window approach. The inner while loop that shrinks the window operates in O(N) time in total since each fruit is removed from the window at most once.

- **Space Complexity**: O(1) - The space used for `window_els` depends on the number of distinct fruits. Since the problem states that there are only two types of fruits that can be collected, the maximum space used is constant. However, in the worst case where the number of distinct fruit types is higher (more than 2), the space complexity could be considered O(2), which simplifies to O(1).

### 3. Why This Approach is Efficient
The sliding window technique is particularly efficient for this problem because it:
- Minimizes unnecessary checks by maintaining a window of valid fruit types, expanding and contracting it dynamically.
- Only processes each fruit in a linear pass, thus ensuring that the solution is optimal with respect to time complexity.
- Operates in-place using a dictionary to keep track of counts, minimizing additional space overhead.

This efficiency makes it suitable for handling large datasets while ensuring the algorithm remains responsive and executes quickly.

Runtime: undefined
Memory: 25900000
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_els = defaultdict(int)
        
        s = 0
        w_l = 0
        for e in range(len(fruits)):
            window_els[fruits[e]] += 1

            while len(window_els) > 2:
                window_els[fruits[s]] -= 1
                if window_els[fruits[s]] == 0:
                    del window_els[fruits[s]]
                s+=1

            w_l = max(w_l, e-s + 1)

            
        return w_l
            
