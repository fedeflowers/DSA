"""
```markdown
# Explanation of the LeetCode Solution for "Longest Balanced Substring II"

## 1. Approach Overview

The solution to the "Longest Balanced Substring II" problem employs a multi-phase strategy to find the longest balanced substring composed of the letters 'a', 'b', and 'c'. A balanced substring is defined as one where the counts of these letters are equal. The solution is divided into five main phases:

- **Phase 1**: Initializes variables and checks for empty input.
- **Phase 2**: Finds runs of the same character, as any single character is trivially balanced.
- **Phase 3**: Examines pairs of letters ('a' and 'b', 'a' and 'c', 'b' and 'c') within segments that do not contain the third letter. This is implemented using a helper function to manage the pair processing.
- **Phase 4**: Uses a 2D prefix difference approach to check for balanced substrings among all three letters. It computes cumulative counts of 'a', 'b', and 'c', storing states based on the difference between their counts.
- **Phase 5**: Returns the length of the longest balanced substring found in any of the phases.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of the solution is O(n), where n is the length of the string `s`. Each character in the string is processed a constant number of times across different phases (either during the direct iteration or while processing segments).
  
- **Space Complexity**: The space complexity is O(n) in the worst case due to the storage of state mappings in a dictionary for phase 4. However, the space requirement is typically close to O(1) for the other processing steps, which mainly use fixed-size variables.

## 3. Efficiency of the Approach

This approach is efficient for multiple reasons:

- **Single Pass for Each Phase**: The use of linear scans eliminates the need for nested loops or excessive recomputation, optimizing the evaluation of balanced substrings.
  
- **Use of Maps for State Tracking**: Leveraging hash maps (dictionaries) allows for quick lookups of previously seen states and differences. This significantly enhances the ability to find matching segments without rescanning the string.

- **Covering All Scenarios**: By separately handling single-letter runs, pairs of letters, and all three characters, the algorithm ensures that all forms of balanced substrings are considered, providing a comprehensive solution.

Overall, the combination of these techniques ensures that the solution is not only correct but also performant, making it suitable for the constraints typically associated with LeetCode problems.
```

Runtime: undefined
Memory: 45484000
"""

class Solution:
    def longestBalanced(self, s: str) -> int:
        # --- Problem: Longest Balanced Substring (Optimized) ---
    # --- Phase 1: Define the optimized function combining three complementary passes ---
        # Handle empty input defensively even though constraints give length >= 1
        if not s:  # Check if the input string is empty, because no substring exists then
            return 0  # Return 0 for empty input, because there is nothing to evaluate

        # Initialize base variables
        n = len(s)  # Cache the length of the string, because we will loop over it multiple times
        max_length = 0  # Track the overall best balanced substring length, because we combine multiple strategies

        # --- Phase 2: Single-letter runs (any run of the same character is balanced) ---
        current_run = 1  # Start with a run length of 1 at the first character, because a single char is a balanced substring
        max_length = 1  # At least one character is always a balanced substring, because one distinct character trivially satisfies equality
        for i in range(1, n):  # Iterate from the second character onward, because we compare with the previous character
            if s[i] == s[i - 1]:  # If the current character matches the previous, because that extends the run
                current_run += 1  # Increase the current run length, because the same character continues
            else:  # Otherwise, the run is broken, because the character changed
                current_run = 1  # Reset the run length to 1 starting at this new character, because a new run begins
            if current_run > max_length:  # If this run exceeds the best length so far, because it may be the answer
                max_length = current_run  # Update the best length, because we found a longer balanced run

        # --- Phase 3: Two-letter equal-count substrings within segments without the third letter ---
        def process_two_letters(first_char: str, second_char: str, breaker_char: str) -> None:  # Define a helper to process one pair, because we need to reuse logic for all pairs
            nonlocal max_length  # Allow updating the outer max_length, because we aggregate results here
            index = 0  # Start scanning from the beginning of the string, because we process all segments
            while index < n:  # Continue until we reach the end, because there may be multiple segments
                while index < n and s[index] == breaker_char:  # Skip over breaker characters, because segments must not contain the third letter
                    index += 1  # Advance the index past breakers, because they delimit segments
                if index >= n:  # If we reached the end after skipping, because no segment remains
                    break  # Exit the loop, because there is nothing left to process
                segment_start = index  # Mark the start of the segment with no breakers, because we will process this region

                # Initialize prefix-difference map for this segment
                diff_to_first_index = {0: segment_start - 1}  # Map difference 0 to the virtual index before segment, because equal counts can start at segment start
                diff = 0  # Running difference (count_first_char - count_second_char), because equal counts correspond to diff repeating

                # Scan the current segment until the next breaker
                while index < n and s[index] != breaker_char:  # Stay within the segment, because breaker marks the end
                    if s[index] == first_char:  # If we see the first tracked character, because it changes the difference
                        diff += 1  # Increment difference for first_char, because it adds +1
                    elif s[index] == second_char:  # If we see the second tracked character, because it also changes the difference
                        diff -= 1  # Decrement difference for second_char, because it adds -1
                    # Note: no else clause is needed because only three characters exist and breaker_char is excluded inside this segment

                    if diff in diff_to_first_index:  # If we have seen this difference before, because equal counts exist between those indices
                        candidate_length = index - diff_to_first_index[diff]  # Compute length from first occurrence to current, because that segment balances the two letters
                        if candidate_length > max_length:  # If this candidate is better than current best, because we seek maximum
                            max_length = candidate_length  # Update the best length, because we found a longer balanced substring
                    else:  # Otherwise, this is the first time we see this difference, because no mapping exists yet
                        diff_to_first_index[diff] = index  # Record the earliest index for this difference, because it helps maximize lengths for future repeats

                    index += 1  # Move to the next character inside the segment, because we continue scanning

                # After finishing this segment, the next iteration will skip the breaker and look for the next segment
                # No additional action is needed here, because variables are reset at the top for each new segment

        # Process all three pairings by excluding the third character each time
        process_two_letters('a', 'b', 'c')  # Balance between 'a' and 'b' when 'c' is absent, because 2-letter balance requires third letter absent
        process_two_letters('a', 'c', 'b')  # Balance between 'a' and 'c' when 'b' is absent, because 2-letter balance requires third letter absent
        process_two_letters('b', 'c', 'a')  # Balance between 'b' and 'c' when 'a' is absent, because 2-letter balance requires third letter absent

        # --- Phase 4: Three-letter equal-count substrings using 2D prefix differences ---
        count_a = 0  # Initialize count for 'a', because we need cumulative counts to form states
        count_b = 0  # Initialize count for 'b', because we need cumulative counts to form states
        count_c = 0  # Initialize count for 'c', because we need cumulative counts to form states
        state_to_first_index = {(0, 0): -1}  # Map the state (a-b, a-c) to earliest index; start with (0,0) at -1, because equal counts from beginning are allowed

        for i, ch in enumerate(s):  # Iterate through each character with index, because we update prefix counts and check states
            if ch == 'a':  # If current char is 'a', because we must increase its count
                count_a += 1  # Increment 'a' count, because we've seen one more 'a'
            elif ch == 'b':  # If current char is 'b', because we must increase its count
                count_b += 1  # Increment 'b' count, because we've seen one more 'b'
            else:  # Otherwise the character is 'c', because the string contains only 'a', 'b', and 'c'
                count_c += 1  # Increment 'c' count, because we've seen one more 'c'

            state = (count_a - count_b, count_a - count_c)  # Compute the 2D difference state, because identical states imply a=b=c on the substring between them
            if state in state_to_first_index:  # If we have seen this state before, because repeating state indicates equal increments of a,b,c in between
                candidate_length = i - state_to_first_index[state]  # Compute the substring length between the two identical states, because counts equalize there
                if candidate_length > max_length:  # If this candidate improves the best length, because we want the maximum
                    max_length = candidate_length  # Update the best length found so far, because we found a longer balanced substring with all three letters
            else:  # If the state has not been seen, because this is the earliest occurrence
                state_to_first_index[state] = i  # Record the earliest index for this state, because it helps form longer substrings when repeated later

        # --- Phase 5: Return the best result found across all phases ---
        return max_length  # Return the maximum length of any balanced substring found, because all passes have completed


