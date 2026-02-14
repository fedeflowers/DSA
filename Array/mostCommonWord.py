"""
```markdown
## Explanation of the LeetCode Solution for "Most Common Word"

### 1. Approach Explanation
The solution to the problem "Most Common Word" consists of the following steps:

- **Normalization**: The input paragraph is converted to lowercase to ensure case-insensitivity. Additionally, all punctuation marks (`!?',;.`) are replaced with spaces, helping to isolate words more effectively.

- **Splitting Words**: The normalized paragraph is then split into individual words based on whitespace.

- **Banned Words Set**: The list of banned words is converted into a set for O(1) average-time complexity lookups.

- **Frequency Map Construction**: A frequency dictionary (`frequency_map`) is built, where each word's occurrence count is recorded (but only for words that are not in the banned set).

- **Finding Most Common Word**: The solution finally iterates over the frequency map to find the word with the highest count and returns it.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
    - Normalizing the paragraph takes O(P), where P is the length of the paragraph, as we iterate through each character to handle case conversion and punctuation removal.
    - Splitting the string into words is O(P) since it involves reading the entire string.
    - Building the frequency map requires O(W) time, where W is the number of words after splitting.
    - Finding the most common word is O(W) since we iterate through the frequency map. 

   Overall, the time complexity is O(P + W), where P is the length of the paragraph, and W represents the number of words (which is generally less than or equal to P).

- **Space Complexity**: 
    - The space complexity is influenced primarily by the storage of the frequency map and the banned words set. The space used for storing words can be O(W) for the frequency map and O(B) for the banned set, where B is the number of banned words.
  
  Therefore, the overall space complexity can be stated as O(W + B).

### 3. Efficiency of the Approach
This approach is efficient because:
- **Linear Passes**: The solution processes the input with a few linear passes, ensuring that time complexity remains manageable even for large inputs.
- **Constant Time Lookups**: Using a set data structure for banned words allows for constant time complexity during lookups, making the algorithm faster as it avoids nested loops.
- **Simplicity and Clarity**: The steps are straightforward and easy to follow, making it maintainable and adaptable for changes.

This efficient handling of normalization, counting, and retrieval ensures that the solution runs within acceptable limits for the constraints typically given in LeetCode problems.
```

Runtime: undefined
Memory: 19488000
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # --- Phase 1: Normalize the paragraph ---
        # Convert the paragraph to lowercase for case-insensitive comparison
        normalized_paragraph = paragraph.lower()  # Ensures all words are lowercase
        # Replace each punctuation character with a space
        for punct in "!?',;.":
            normalized_paragraph = normalized_paragraph.replace(punct, ' ')  # Removes punctuation for clean splitting
        
        # --- Phase 2: Split into words ---
        words = normalized_paragraph.split()  # Splits the paragraph into words by whitespace
        
        # --- Phase 3: Prepare banned set for O(1) lookup ---
        banned_set = set(banned)  # Allows fast checking if a word is banned
        
        # --- Phase 4: Build frequency map for non-banned words ---
        frequency_map = {}  # Dictionary to store word frequencies
        for word in words:  # For each word in the list
            if word not in banned_set:  # Only count if not banned
                if word in frequency_map:
                    frequency_map[word] += 1  # Increment count if already present
                else:
                    frequency_map[word] = 1  # Initialize count if first occurrence
        
        # --- Phase 5: Find the word with the highest frequency ---
        max_count = 0  # Track the highest frequency
        most_common = ''  # Track the corresponding word
        for word, count in frequency_map.items():  # For each word and its count
            if count > max_count:  # If this word's count is higher
                max_count = count  # Update the highest frequency
                most_common = word  # Update the most common word
        return most_common  # Return the most frequent non-banned word

