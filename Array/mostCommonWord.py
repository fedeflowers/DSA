"""
```markdown
## Explanation of the Approach

The solution to the "Most Common Word" problem employs the following steps:

1. **Initialization**: The list of banned words is converted into a set for O(1) average time complexity during lookups.
   
2. **Normalization**: The input paragraph is converted to lower case to ensure uniformity, allowing case-insensitive comparisons. Special punctuation marks are then replaced with spaces to isolate words.

3. **Word Splitting**: The normalized paragraph is split into individual words based on spaces.

4. **Counting Words**: A `Counter` from the `collections` module is used to count the occurrences of each word in the list. This creates a dictionary-like object where the words are keys, and their counts are the corresponding values.

5. **Finding the Most Common Word**: The program iterates through the counted words, skipping any words that are in the banned set. For each remaining word, it checks if its count is greater than the maximum count recorded so far. If it is, the current word is stored as the most frequent word.

6. **Return the Result**: Finally, the most common non-banned word is returned.

## Time and Space Complexity Analysis

- **Time Complexity**: 
  - Normalizing the paragraph takes O(P), where P is the length of the paragraph.
  - Splitting the paragraph into words takes O(W), where W is the number of words.
  - Counting occurrences with `Counter` is O(W).
  - Iterating through the counted words is O(U), where U is the number of unique words. 
  - Overall, the time complexity can be approximated as O(P + W) since P will generally be larger than W.

- **Space Complexity**: 
  - The space used by the `Counter` will depend on the number of unique words U, giving a space complexity of O(U).
  - The set of banned words uses O(B), where B is the number of banned words.
  - Therefore, the total space complexity is O(U + B).

## Why This Approach is Efficient

This approach is efficient due to the following reasons:

1. **Use of Sets for Banned Words**: Converting the list of banned words to a set allows for average O(1) time complexity lookups, making the filtering process quick and efficient.

2. **Normalization and Word Counting**: By utilizing built-in Python functionalities (`replace`, `split`, and `Counter`), the code is concise and leverages optimized implementations for string manipulation and counting, reducing the need for complex loops.

3. **Single Pass for Most Common Word**: The final search for the most common word only requires a single pass through the counted words, ensuring that the overall operation remains linear in relation to the number of words.

This combination of efficient data structures and optimized operations results in a solution that effectively handles the requirements of the problem within reasonable time and space limits.
```

Runtime: undefined
Memory: 19608000
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        
        normalized_paragraph = paragraph.lower()
        for punct in "!?',;.-#":
            normalized_paragraph = normalized_paragraph.replace(punct, " ")
            
        words = normalized_paragraph.split()
        
        counted_words = Counter(words)
        max_count = 0
        most_freq_w = ""
        for w, v in counted_words.items():
            if w in banned:
                continue
            if v > max_count:
                max_count = v
                most_freq_w = w
        
        return most_freq_w
