"""
```markdown
# Longest Palindromic Substring Solution Explanation

## 1. Approach

The solution uses the "expand around center" technique to find the longest palindromic substring in the given string `s`. It considers each character and each pair of characters as potential centers of a palindrome and expands outwards as long as the characters at the expanding indices are the same.

Here's how the code works:

- The main function `longestPalindrome` initializes a helper function `expand(l, r)` that expands around the indices `l` and `r` as long as the characters at those indices are equal.
- For each position in the string (from index `0` to `len(s) - 1`), it tries to find palindromes:
  - First, it checks for palindromes with a single center (`expand(i, i)`), which accounts for odd-length palindromes.
  - Then, it checks for palindromes with two centers (`expand(i, i + 1)`), which accounts for even-length palindromes.
- It keeps track of the longest palindrome found by updating the tuple `max_palin` that stores the start and end indices of the longest palindrome substring.
- Finally, the substring identified by `max_palin` is returned.

## 2. Time and Space Complexity Analysis

- **Time Complexity:** O(n^2)
  - The main loop runs for `n` iterations (where `n` is the length of the string). For each iteration, the `expand` function can take up to `O(n)` time in the worst case (if the entire string is a palindrome).
  
- **Space Complexity:** O(1)
  - The solution uses a constant amount of space for variables (like indices and the `max_palin` tuple). The space used for the return value is not counted in space complexity since it's dependent on the input size.

## 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Direct Expansion:** By expanding from the center, it directly accesses palindrome properties without additional data structures like dynamic programming tables or sets.
- **No Redundant Checks:** Each character and every potential pair of characters are checked only once, avoiding the redundancy found in other methods such as checking all possible substrings.
- **Simple Implementation:** The method is straightforward to implement and follows a logical flow, making it easy to understand and maintain.

In summary, the "expand around center" technique is an effective way to find the longest palindromic substring with a manageable time complexity and minimal space requirements.
```

Runtime: undefined
Memory: 17176000
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #expand from center for each position
        def expand(l,r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return l+1, r-1
                l-=1
                r+=1
            return l+1,r-1

        max_palin = (0,0)
        for i in range(len(s)):
            l,r = expand(i,i)
            if r-l+1 > max_palin[1] - max_palin[0] + 1:
                max_palin = (l,r)
            l1,r1 = expand(i,i+1)
            if r1-l1+1 > max_palin[1] - max_palin[0] + 1:
                max_palin = (l1,r1)

        return s[max_palin[0]:max_palin[1]+1]



