"""
# Explanation of the "Valid Parentheses" Solution

## 1. Approach

The solution to the "Valid Parentheses" problem uses a stack data structure to keep track of the opening parentheses as they are encountered. The core idea is to ensure that every opening parenthesis has a corresponding closing parenthesis in the correct order. Here’s a brief breakdown of the approach:

- **Initialize a stack**: Create an empty list (`stack`) that will store opening parentheses.
- **Mapping dictionary**: Define a dictionary (`d`) that maps each type of closing parenthesis to its corresponding opening one, i.e., `")"` maps to `"("`, `"]"` maps to `"["`, and `"}"` maps to `"{"`.
- **Iterate through the string**: Loop through each character `c` in the input string `s`:
  - If `c` is an opening parenthesis (present in the dictionary values), push it onto the stack.
  - If `c` is a closing parenthesis:
    - Check if the stack is empty. If it is, return `False` because there is no matching opening parenthesis.
    - If the stack is not empty, pop the last element (`last_el`) from the stack and check if it matches the opening parenthesis for the closing `c` using the mapping dictionary. If they do not match, return `False`.
- **Final check**: After processing all characters, check if the stack is empty. If it is, it means all opening parentheses had matching closing ones; hence return `True`. If not, return `False`.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the string `s`. In the worst case, the algorithm has to traverse the entire string once.
  
- **Space Complexity**: O(n) in the worst case, which occurs when all characters in the string are opening parentheses (i.e., there are no closing parentheses). The stack will grow to store all of them.

## 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Single Pass**: The algorithm processes the string in a single pass (O(n)), ensuring it operates efficiently even for larger strings.
- **Constant Time Operations**: Stack operations (push, pop) are O(1), making it quick to manage the opening parentheses as they are tracked.
- **Direct Use of Data Structures**: The use of a stack aligns perfectly with the problem requirement of matching pairs, allowing a straightforward management of nested structures (like parentheses) without needing additional checks.
- **Immediate Feedback**: The function can immediately return `False` if an unmatched closing parenthesis is found, minimizing unnecessary checks after invalid input is detected.

Overall, the algorithm is simple, clear, and effectively addresses the problem using well-established data structure principles.

Runtime: undefined
Memory: 19316000
"""

class Solution:
    def isValid(self, s: str) -> bool:
        #()[]{()}
        #
        stack = []
        d = {")": "(", "]": "[", "}":"{"}
        for c in s:
            if c in d.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    last_el = stack.pop()
                    if d[c] != last_el:
                        return False
                    
        return len(stack) == 0
            
