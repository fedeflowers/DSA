"""
# Explanation of LeetCode Solution for "Valid Palindrome II"

## 1. Approach Explanation

The problem "Valid Palindrome II" asks whether a given string can become a palindrome by removing at most one character. The provided solution implements an iterative approach to solve this problem.

- The algorithm uses two pointers, `l` (left) and `r` (right), which start at the beginning and end of the string respectively.
- While the left pointer is less than the right pointer:
  - It compares the characters at the two pointers:
    - If `s[l]` is not equal to `s[r]`, this indicates a mismatch. 
      - To verify if the string can be a palindrome after removing one character, it checks two scenarios:
        1. Ignoring the character at the left pointer (`s[l]`), i.e., checking the substring from `l + 1` to `r`.
        2. Ignoring the character at the right pointer (`s[r]`), i.e., checking the substring from `l` to `r - 1`.
      - It checks if either substring is a palindrome by comparing it with its reverse.
    - If the characters are equal, it simply moves both pointers inward (`l` increments and `r` decrements).
- If all characters match throughout the loop without encountering more than one mismatch, the function returns `True`, indicating that the string can be a palindrome.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The loop itself runs at most `O(N)` where `N` is the length of the string, as each character is checked once.
  - The palindrome check for substrings (`skip_l == skip_l[::-1]` and `skip_r == skip_r[::-1]`) each take `O(N)` in the worst case, when these substrings include nearly the entire string. Therefore, the overall time complexity in the worst case could be approximated to `O(N)` due to the predominant linear traversal, as the palindrome checks will short-circuit on a valid comparison before needing to evaluate the full string reversal.

- **Space Complexity**: 
  - The algorithm uses a constant amount of extra space (i.e., two pointers and substrings that do not add persistent storage). Thus, the space complexity is `O(1)`, apart from the space used to hold the input string.

## 3. Efficiency of the Approach

This iterative approach is efficient because:
- It leverages two pointers to traverse the string, avoiding the overhead of deep recursion that might occur in a recursive solution.
- The worst-case time complexity is linear `O(N)`, making it suitable for sufficiently large input sizes.
- The immediate dismissal of paths (after the first mismatch) that do not yield a palindrome keeps the algorithm responsive and improves average case performance.
- By checking only two substrings, the solution reduces unnecessary calculations, ensuring that only required comparisons are made.

Overall, this approach balances clarity and efficiency, making it an optimal choice for solving the problem of valid palindromes with the allowance of one character removal.

Runtime: undefined
Memory: 18040000
"""

# RECURSIVE
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def palin(s, start, end, errors):
#             if errors < 0 :
#                 return False
#             if start > end:
#                 return True
#             if s[start] != s[end]:
#                 return palin(s, start + 1, end, errors-1) or palin(s, start, end-1, errors-1)
#             return palin(s, start +1, end-1, errors)

#         return palin(s, 0, len(s)-1, 1)

# ITERATIVE
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # If mismatch, check if skipping Left OR skipping Right creates a palindrome
                skip_l = s[l+1:r+1] 
                skip_r = s[l:r]
                return (skip_l == skip_l[::-1]) or (skip_r == skip_r[::-1])
            l += 1
            r -= 1
            
        return True
