"""
```markdown
# Explanation of the "Valid Palindrome" Solution

## 1. Approach
The given solution aims to determine if a string is a valid palindrome by following these steps:

1. **Cleaning the Input**: It initializes an empty string called `clean`. The solution iterates over each character in the input string `s`, appending only alphanumeric characters (letters and numbers) to `clean`, while converting them to lowercase. This ensures that the palindrome check is case-insensitive and ignores non-alphanumeric characters (e.g., spaces, punctuation).

2. **Two-Pointer Technique for Palindrome Check**: Once we have the cleaned string, the solution uses two pointers (`s` for the start and `e` for the end of the string). It compares the characters at these two pointers:
   - If they are not equal, it immediately returns `False`, indicating the string is not a palindrome.
   - If they are equal, the pointers are moved toward the center (`s` is incremented and `e` is decremented), and the process repeats until the pointers cross each other.

3. **Final Check**: If all the character comparisons are successful (meaning all pairs of characters from both ends match), the function returns `True`, indicating that the string is a valid palindrome.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - The code iterates through the input string `s` once to clean it, which takes O(N), where N is the length of string `s`.
  - It then iterates through the cleaned string with the two-pointer technique, which takes O(M), where M is the length of the cleaned string. In the worst case, M is proportional to N, leading to an overall time complexity of O(N).

- **Space Complexity**: O(M)
  - The space complexity is determined by the storage of the cleaned string `clean`, which can be up to O(N) in the worst case where all characters are alphanumeric. 

## 3. Efficiency of the Approach
- **Efficiency of Character Filtering**: The approach effectively filters out unwanted characters and reads the input string only twice (once for filtering and once for checking the palindrome). This leads to an efficient way to handle potentially large strings.

- **Early Exit**: By checking characters from both ends towards the center, it allows for an immediate exit (returning `False`) as soon as a mismatch is found, thus potentially saving unnecessary comparisons.

- **Simplicity**: The logic is straightforward and easy to follow, making the code clean and maintainable. The use of the two-pointer technique is both intuitive and effective in checking for palindromes.

Overall, this solution is both efficient and easy to understand, making it a suitable choice for the problem at hand.
```

Runtime: undefined
Memory: 19516000
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        s, e = 0, len(clean)-1
        while s< e:
            if clean[s] != clean[e]:
                return False
            s += 1
            e -= 1
        return True
