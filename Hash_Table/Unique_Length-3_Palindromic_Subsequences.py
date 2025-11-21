"""
```markdown
## Explanation of the Solution for Unique Length-3 Palindromic Subsequences

### 1. Approach Explanation
The problem requires counting unique length-3 palindromic subsequences in a given string `s`. A length-3 palindromic subsequence has the form `aba`, where `a` is any character and `b` is any character that differs from `a`.

The solution iterates over each unique character in the string and identifies its first and last occurrence. If these occurrences allow for characters to exist in between (`last > first + 1`), it counts the number of unique characters located between these two indices. These unique characters serve as potential `b` candidates in the palindromic structure `aba`.

The step-by-step core of the approach is as follows:
- For each unique character (`char`), find its first (`first`) and last (`last`) occurrence in the string.
- Check if there is space between `first` and `last`. If yes, count the unique characters in the substring that exists between those indices.
- Each unique character found in this space contributes to the creation of a unique palindromic subsequence of the form `char + b + char`.

The final result is the accumulated count of all such valid configurations for each unique character in the string.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n * k), where `n` is the length of the string, and `k` is the number of unique characters in `s`. 
  - For each unique character, the solution performs `find` and `rfind` which are O(n) operations, and subsequently computes the length of a set formed from the substring (also O(n) in the worst case, but as it only iterates through a segment of `s`, it's also on the order of n).
  
- **Space Complexity**: O(k), where `k` is the number of unique characters in the string, since we store unique characters in a set to count them effectively.

### 3. Efficiency of the Approach
This approach efficiently narrows down the candidates for the middle character `b` by capitalizing on positions where potential palindromic subsequences can exist. 

Compared to a brute force approach that would explore all combinations of indices (which could lead to a vast number of checks given that a subsequential approach could retrieve results multiple times), this optimized method ensures that we only focus on sections of the string where valid palindromic structures may exist. By leveraging the positions of characters, the algorithm avoids unnecessary computations, resulting in improved performance, especially for longer strings.

Overall, by using `set` to count unique characters and systematically checking character spaces, this approach balances clarity and efficiency, making it effective for the problem.
```

Runtime: N/A
Memory: N/A
"""

# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
        #brute force
        # res = set()
        # n = len(s)
        # def rec(curr, index):
        #     if len(curr) == 3 and curr == curr[::-1]:
        #         res.add(curr)
        #     if len(curr) > 3:
        #         return
        #     if index >= n:
        #         return
        #     if curr in res:
        #         return

        #     rec(curr + s[index], index + 1) #take
        #     rec(curr, index + 1) #not take
            
        # rec("", 0)

        # return len(res)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        # Iterate over every unique character as a potential "outer" layer
        for char in set(s):
            first, last = s.find(char), s.rfind(char)
            
            # If there is space between the first and last occurrence
            if last > first + 1:
                # Add the count of unique characters between them
                res += len(set(s[first + 1 : last]))
                
        return res
