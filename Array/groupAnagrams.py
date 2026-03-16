"""
# Explanation of the LeetCode Solution for "Group Anagrams"

## 1. Brief Explanation of the Approach
The problem of grouping anagrams involves taking a list of strings and organizing them into groups where each group contains words that are anagrams of each other. An anagram is a word formed by rearranging the letters of another.

In the provided code solution:

- A `defaultdict` from the `collections` module is used to create a hash map (`hsh`) where the key is a tuple representing the sorted characters of a word, and the value is a list of words (anagrams) that correspond to that key.
- For each word in the input list `strs`, the solution sorts the characters in the word and converts the sorted list of characters into a tuple. This sorted tuple serves as a unique identifier for anagrams since all anagrams of a word will result in the same sorted tuple.
- The word is then appended to the list stored in the dictionary at the key of the sorted tuple.
- Finally, the solution returns the values of the dictionary, which are lists of grouped anagrams.

## 2. Time and Space Complexity Analysis

### Time Complexity
- Sorting each word takes \(O(K \log K)\) time, where \(K\) is the maximum length of a word in the input list.
- If there are \(N\) words in the input list, the overall time complexity for sorting all words can be expressed as \(O(N \times K \log K)\).

### Space Complexity
- The space complexity is \(O(NK)\), where \(N\) is the number of words and \(K\) is the maximum length of a word. This accounts for storing each word in the hash map and the tuples created for each sorted word.

## 3. Why This Approach is Efficient
The solution is efficient for several reasons:

- **Use of Sorting for Anagram Identification**: By sorting the characters of each word, the solution allows for easy grouping of anagrams. This method ensures that all permutations of a word converge to the same sorted tuple.
- **Hash Map for Grouping**: Utilizing a `defaultdict` provides an efficient and simple way to group words. The average time complexity for insertions into a hash map is \(O(1)\).
- **Overall Manageability**: The overall complexity is manageable given the operations performed. While sorting is inherently \(O(K \log K)\), the approach remains efficient for reasonable word and list sizes.
- **Scalability**: The algorithm can efficiently handle various input sizes due to its straightforward structure, making it ideal for use in competitive programming and real-world applications where grouping data is required.

The combination of sorting and hash maps leads to an elegant solution to the "Group Anagrams" problem, effectively balancing readability, performance, and maintainability.

Runtime: undefined
Memory: 22616000
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = defaultdict(list)
        for word in strs:
            hsh[tuple(sorted(word))].append(word)


        return list(hsh.values())
