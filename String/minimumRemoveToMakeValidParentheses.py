"""
```markdown
# Explanation of LeetCode Solution for "Minimum Remove to Make Valid Parentheses"

## 1. Brief Explanation of the Approach
The provided solution aims to make a string of parentheses valid by removing the minimum number of invalid parentheses. The algorithm operates in two main phases:

1. **Tracking Invalid Closing Parentheses**: 
   - It uses a stack to keep track of the indices of unmatched opening parentheses `'('`.
   - For each character in the string, if it encounters an opening parenthesis `'('`, it pushes its index onto the stack.
   - For every closing parenthesis `')'`, if the stack is not empty (indicating a matching opening parenthesis is available), it pops from the stack. If the stack is empty, it marks the current index (i.e., invalid closing parenthesis) to be removed by setting `chars[i]` to an empty string.

2. **Removing Unmatched Opening Parentheses**:
   - After processing all characters, any remaining indices in the stack indicate unmatched opening parentheses. These are also marked for removal by setting `chars[i]` to an empty string.

Finally, the modified list of characters is joined back into a string and returned.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: `O(N)`
  - The algorithm processes the string in a single pass to mark invalid parentheses and performs another pass over the indices in the stack. Each operation is linear with respect to the length of the input string `N`.
  
- **Space Complexity**: `O(N)`
  - In the worst case, where the string consists only of opening or closing parentheses, the stack can grow to contain all `N` indices, and the `chars` list requires `O(N)` space to store the characters.

## 3. Why this Approach is Efficient
This approach is efficient due to its linear traversal of the input string to identify and remove invalid parentheses. By using a stack to track indices, the solution is able to effectively manage the opening and closing pairs without needing nested loops or backtracking:

- **Single-pass operation**: The method processes the string in two linear sweeps, ensuring that we check and manage the parentheses in a straightforward manner.
- **Direct Modification**: It modifies the original characters in place rather than constructing multiple intermediate strings, which keeps space utilization under control.

Overall, the design of tracking indices using a stack ensures optimal performance in terms of both time and space relative to the problem's constraints.
```

Runtime: undefined
Memory: 20580000
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        for i, char in enumerate(chars):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''


        for i in stack:
            chars[i] = ''
        return ''.join(chars)

