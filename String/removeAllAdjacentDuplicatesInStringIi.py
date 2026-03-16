"""
```markdown
## Explanation of the Solution

The problem "Remove All Adjacent Duplicates in String II" requires removing adjacent characters in a string that occur consecutively `k` times. The provided solution effectively handles this by using a stack data structure to track characters and their counts.

### 1. Approach Explanation

The algorithm iterates through each character in the input string `s`. It uses a stack where each entry is a list containing a character and its count of consecutive occurrences. The steps are as follows:

- **Iterate through each character in the string**:
  - If the stack is not empty and the top of the stack has the same character as the current character, it increments the count of that character.
    - If the count reaches `k`, it pops the character from the stack (removing the adjacent duplicates).
  - If the character is different (or the stack is empty), it pushes a new entry to the stack with the character and initializes its count to `1`.
  
- After processing all characters, the stack contains characters that are not removed. The final output string is constructed by concatenating characters multiplied by their counts.

### 2. Time and Space Complexity

- **Time Complexity**: The algorithm runs in O(N), where N is the length of the string. Each character is processed once, with constant-time operations (push, pop) associated with the stack.

- **Space Complexity**: The space complexity is O(N) in the worst case. In the case where no characters are removed (i.e., all characters are unique or fewer than `k` consecutive characters), the stack will contain all characters.

### 3. Why This Approach is Efficient

This approach is efficient for the following reasons:

- **Optimized Processing**: Instead of recreating the string multiple times (which could be costly), it uses a stack to keep track of character counts in a single pass. Thus, operations are minimized and made more efficient.
  
- **Dynamic Management**: The use of a stack allows for dynamic management of characters and their counts, which means that as soon as a character reaches a count of `k`, it is immediately removed without the need to revisit earlier parts of the string.

- **Scalability**: Since the solution runs in linear time and uses stack operations that are inherently efficient, it can handle larger strings effectively compared to more naive methods that might recheck parts of the string multiple times.

Overall, this stack-based algorithm offers a compact and efficient way to solve the problem while ensuring that the solution can scale with input size.
```

Runtime: undefined
Memory: 23956000
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # brute force = simulation
        # recreation of string = slow, flag characters instead?
        # compress and then recompute? 1a1b1c1d -> ok use stack
        stack = []
        for c in s:
            if stack and stack[-1][0] == c: #
                stack[-1][-1] += 1
                if stack[-1][-1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])

        return "".join([c*num for c, num in stack])

