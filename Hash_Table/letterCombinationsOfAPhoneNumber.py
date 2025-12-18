"""
# Explanation of the LeetCode Solution for "Letter Combinations of a Phone Number"

## 1. Brief Explanation of the Approach

The provided solution utilizes a backtracking approach to generate all possible letter combinations that can be formed from a given string of digits, mapping each digit to its corresponding letters on a phone keypad. The `mapping` dictionary defines which letters correspond to each digit (from 2 to 9).

### Function Breakdown:
- **letterCombinations**: This is the main function that initializes the mapping and prepares to collect results. It defines a helper function `backtrack`.
- **backtrack**: This is a recursive helper function that explores all potential letter combinations:
  - It takes two parameters: `path` (a temporary list to build the current combination) and `i` (the current index in the digits string).
  - If `i` is equal to the length of `digits`, it means a valid combination has been formed; thus, it joins the `path` into a string and appends it to `all_combs`.
  - If not, it iterates through each character in the mapped string for the current digit, appends the letter to `path`, and recursively calls itself to continue building the combination. After exploring that path, it removes the last character (backtracking) to explore other possibilities.

Finally, after exploring all combinations, it returns the list of combinations in `all_combs`.

## 2. Time and Space Complexity Analysis

### Time Complexity:
The time complexity of this solution is \(O(4^N)\), where \(N\) is the number of digits in the input. This is because:
- In the worst case, each digit can map to at most 4 letters (for digits 7 and 9). Therefore, the total number of combinations will be roughly \(4^N\).
  
### Space Complexity:
The space complexity of this solution is \(O(N)\) due to:
- The space used for the `path` variable as it holds up to \(N\) characters (with \(N\) being the number of digits).
- The space used to store the result list `all_combs` which will eventually hold \(O(4^N)\) string combinations, but the maximum space used at any given time during a single recursive call stack will be linear to the depth of the recursion, which is \(O(N)\).

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:
- **Backtracking**: The use of backtracking allows this algorithm to explore all combinations in a systematic way, avoiding unnecessary computations. It only constructs combinations that are valid, pruning the search tree when necessary.
- **Simple and Readable**: The implementation is straightforward, making it easy to understand and maintain. The mapping dictionary clearly represents the relationships between digits and letters.
- **Scalability**: The algorithm can handle varying lengths of input digits naturally. While the time complexity grows exponentially with the number of digits, it handles real-world constraints well for moderate input sizes, which is typical in coding interviews.

Overall, the combination of backtracking and a clear mapping enables the algorithm to find all possible combinations efficiently, underlying a practical and effective solution for generating letter combinations from phone number inputs.

Runtime: undefined
Memory: 17528000
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        all_combs = []
        def backtrack(path, i):
            if i == len(digits):
                all_combs.append("".join(path))
                return

            for c in mapping[int(digits[i])]:
                path.append(c)
                backtrack(path, i+1)
                path.pop() 

        backtrack([], 0)
        return all_combs
