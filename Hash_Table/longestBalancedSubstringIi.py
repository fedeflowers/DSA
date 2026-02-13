"""
# Solution Explanation for "Longest Balanced Substring II"

## 1. Approach Explanation

The solution employs a three-phase strategy to find the longest balanced substring containing the characters 'a', 'b', and 'c'. 

- **Phase 1: Single-letter Runs**
  - The algorithm first identifies the longest contiguous segment of a single character (either 'a', 'b', or 'c'). Since any continuous run of a single letter is trivially balanced in the sense that it has equal counts (namely, something like `aaaa` can be seen as balanced since it's exclusively composed of 'a'), the length of the longest contiguous substring is initialized as `max_length`.

- **Phase 2: Double-letter Balanced Substrings**
  - The solution then defines a helper method `process_pair(x, y)` that calculates the longest substring balanced between two specific characters. The method uses a frequency difference count to find segments in which the counts of 'x' and 'y' are equal. It resets the count whenever a character that is neither 'x' nor 'y' is encountered. The difference helps to identify positions where the counts of 'x' and 'y' return to their initial state, indicating a balanced substring.

- **Phase 3: Three-letter Equal-Count Substrings**
  - Finally, it checks for substrings where the counts of all three characters 'a', 'b', and 'c' are equal using a two-dimensional difference state representation `(a-b, a-c)`. This method tracks cumulative counts of 'a', 'b', and 'c' and checks if this 2D state has been seen before. If it has, the substring between the previous and current indices has equal counts of 'a', 'b', and 'c'.

The solution returns the maximum length found across all three phases.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(n)
  - The algorithm iterates over the string a constant number of times (three main passes: one for single-letter runs, one for each of the three pairs in double-letter balanced substrings, and one for the three-letter case). Each pass generally handles each character only a limited number of times across the respective segments, yielding an overall complexity linear with respect to the length of the string `n`.

- **Space Complexity**: O(1) 
  - The space used is for a fixed number of variables and mappings (e.g., dictionary for indices and counts), independent of the input size. Thus, the space usage remains constant regardless of the input's length.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Single Pass Scanning**: Each character is processed in a single traversal for determining runs and balanced substrings, minimizing additional overhead and avoiding nested loops.

- **Use of Prefix Counts**: By using cumulative counts and differences, the solution effectively reduces the complexity of finding balanced segments, leveraging hash maps for quick look-up and insertion.

- **Direct Handling of All Cases**: The algorithm efficiently handles single, double, and triple character cases within the same framework, providing maximum flexibility without needing extra data structure overhead.

- **Avoidance of Redundancy**: The algorithm ensures that once a character is not part of the current pair, it resets and doesn't count towards future substrings. This method prevents unnecessary calculations and optimizes performance.

Overall, this structured approach combines clarity with optimal performance, effectively addressing the problem requirements while ensuring scalability.

Runtime: undefined
Memory: 45200000
"""

class Solution:
    def longestBalanced(self, s: str) -> int:
        # --- Function: Longest Balanced Substring (Optimized) ---
        # Handle edge case: empty string -> no substrings, so return 0 directly
        if not s:  # Check if the input string is empty
            return 0  # Return 0 because there cannot be any balanced substring in an empty string

        # Cache length and a mapping from character to index to simplify counting logic
        n = len(s)  # Store length to avoid repeated len() calls and to guide loops
        index_of = {'a': 0, 'b': 1, 'c': 2}  # Fixed mapping for clarity and O(1) count updates

        # Initialize the answer; we'll take the maximum across different strategies
        max_length = 0  # Start with 0 and update as we find longer balanced substrings

        # --- Phase 1: Single-letter runs are trivially balanced ---
        current_run_char = None  # Track the character in the current run to detect changes
        current_run_length = 0  # Track the length of the current contiguous run
        for ch in s:  # Iterate over each character to measure runs
            if ch == current_run_char:  # If the character matches the current run's character
                current_run_length += 1  # Extend the run because the same character continues
            else:  # The character changed, so we start a new run
                current_run_char = ch  # Update the run character to the new one
                current_run_length = 1  # Reset the run length to 1 for the new run
            if current_run_length > max_length:  # Check if this run is the longest balanced substring so far
                max_length = current_run_length  # Update the global maximum because single-letter runs are balanced

        # --- Phase 2: Exactly-two-letter balanced substrings via per-pair scans ---
        def process_pair(x: str, y: str) -> int:
            """Return the longest substring length containing only x and y with equal counts."""  # Explain purpose for clarity
            diff = 0  # Initialize the prefix difference count(x) - count(y) to zero before scanning
            first_occurrence = {0: -1}  # Map each seen diff to its earliest index; start with diff=0 at virtual index -1
            best = 0  # Track the best length found within this pair across the whole string
            for i, ch in enumerate(s):  # Scan the entire string once
                if ch != x and ch != y:  # If we encounter the third letter, this breaks the two-letter condition
                    diff = 0  # Reset diff because substrings cannot cross this boundary (would include a third letter)
                    first_occurrence = {0: i}  # Reset the map; treat boundary as index i so next segment starts at i+1
                    continue  # Skip updates for this index since ch is not part of the {x,y} pair
                # Update diff based on whether we saw x or y in this position
                if ch == x:  # If current char is the first of the pair
                    diff += 1  # Increase diff to reflect one more x than y in the prefix up to i
                else:  # Otherwise the char must be y (since non-pair case already continued)
                    diff -= 1  # Decrease diff to reflect one more y than x in the prefix up to i
                # If we've seen this diff before within the current segment, we found a zero-sum subarray (equal counts)
                if diff in first_occurrence:  # Check for previous occurrence of the same diff value
                    length = i - first_occurrence[diff]  # Compute the substring length between the two occurrences
                    if length > best:  # If this substring is longer than the best seen for this pair
                        best = length  # Update the best because we found a longer balanced two-letter substring
                else:  # First time we see this diff in the current segment
                    first_occurrence[diff] = i  # Record the earliest index for this diff to maximize future lengths
            return best  # Return the best length for this pair across all segments

        # Compute best equal-count substrings for each pair and update the global maximum accordingly
        max_length = max(max_length, process_pair('a', 'b'))  # Update with the best balanced substring using only 'a' and 'b'
        max_length = max(max_length, process_pair('a', 'c'))  # Update with the best balanced substring using only 'a' and 'c'
        max_length = max(max_length, process_pair('b', 'c'))  # Update with the best balanced substring using only 'b' and 'c'

        # --- Phase 3: All-three-letter equal-count substrings via 2D prefix-difference state ---
        counts = [0, 0, 0]  # Initialize prefix counts for 'a', 'b', and 'c' to zero
        state_to_first_index = {(0, 0): -1}  # Map 2D state (a-b, a-c) to earliest index; start with origin at -1
        for i, ch in enumerate(s):  # Walk through the string once
            counts[index_of[ch]] += 1  # Update the appropriate count to include s[i] in the prefix
            state = (counts[0] - counts[1], counts[0] - counts[2])  # Compute the 2D state capturing pairwise diffs to 'a'
            if state in state_to_first_index:  # If we've seen this state before, the substring between has equal deltas
                length = i - state_to_first_index[state]  # Compute substring length achieving equal counts of a, b, and c
                if length > max_length:  # Compare against the global maximum
                    max_length = length  # Update the answer because we found a longer balanced 3-letter substring
            else:  # First time this state appears
                state_to_first_index[state] = i  # Record earliest index to maximize future substring lengths for this state

        # Return the longest balanced substring length found across all strategies
        return max_length  # This is the final answer combining single, double, and triple-letter cases

