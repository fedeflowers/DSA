"""
```markdown
## Explanation of the Zigzag Conversion Solution

### 1. Brief Explanation of the Approach
The goal of the "Zigzag Conversion" problem is to arrange characters of a given string in a zigzag pattern across a specified number of rows and then read the characters line by line to produce the final string output.

The provided solution follows these steps:

- **Base Case**: If `numRows` is 1, the method returns the original string `s` as there's no zigzag pattern needed.
  
- **Matrix Initialization**: A list of lists (a matrix) named `matrix` is created, where each list corresponds to a row in the zigzag pattern. There are `numRows` lists initialized to store characters.

- **Character Placement**: A single variable `c` tracks the current row, which begins at 0. A variable `step` controls whether we move down or up in the zigzag:
  - If `c` equals `numRows-1`, `step` is set to -1 (to move up).
  - If `c` equals 0, `step` is set to 1 (to move down). 
- The characters from the string `s` are appended to the appropriate row in `matrix` based on the current row index `c`. After each placement, `c` is updated based on `step`.

- **Constructing the Result**: Once all characters are placed into `matrix`, each sublist (row) is combined into a single string. Finally, these strings are concatenated together to form the resultant string, which represents the zigzag conversion.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity is O(N), where N is the length of the string `s`. Each character of the string is processed exactly once to determine its final position.
  
- **Space Complexity**: The space complexity is O(N) as well, since we create a 2D list (`matrix`) of size proportional to the length of the string to hold the characters. In the worst case, if `numRows` is large, this still grows linearly with the input string length.

### 3. Why This Approach is Efficient
The approach is efficient for several reasons:
- **Linear Pass**: The solution makes a single pass over the string, ensuring that each character is processed only once. This minimizes time spent on manipulation.
- **Direct Mapping**: By using the row-count and a direction indicator (`step`), we directly map characters to their respective positions instead of requiring additional manipulations or lookups.
- **Dynamic Storage**: The list of lists structure allows for straightforward appending of characters without worrying about initial size allocation, which is beneficial when processing varying input sizes.

Overall, this solution is both time-efficient and space-efficient, adhering to optimal algorithm design principles.
```

Runtime: undefined
Memory: 18068000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        matrix = [[] for i in range(numRows)]
        c=0
        for i in range(len(s)):
            if c == numRows-1:
                step = -1
            if c == 0:
                step = 1
            matrix[c].append(s[i])
            c += step
        m = [''.join(row) for row in matrix]
        res = ''.join(m)
        return res
         
        
