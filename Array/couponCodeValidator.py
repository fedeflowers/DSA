"""
## Explanation of the Approach

The provided solution validates coupon codes based on a series of criteria: 
1. The coupon ID must contain only valid characters.
2. The associated business line must be one of the permitted types.
3. The coupon must be marked as active.

### Steps in the Approach:
1. **Character Validation**:
   - A set of valid characters (`valid_chars`) is created, including:
     - Lowercase letters ('a' to 'z')
     - Uppercase letters ('A' to 'Z')
     - Digits ('0' to '9')
     - An underscore ('_')
   
2. **Validation Function**:
   - A helper function `is_valid(id)` is defined, which checks if all characters in the coupon ID are within the `valid_chars`. It returns `True` if valid, otherwise `False`.
   
3. **Business Validation**:
   - A set `valid_businesses` is defined, containing the valid business lines: `"electronics"`, `"grocery"`, `"pharmacy"`, and `"restaurant"`.

4. **Iterating Through Coupons**:
   - The function iterates through each coupon ID, business line, and active status in tandem using the `zip` function.
   - For each coupon, it checks:
     - If the coupon ID is valid.
     - If the business line is valid.
     - If the coupon is active.
   - Valid coupons are appended to a list `valid_coupons` in the format `[id, business, active]`.

5. **Sorting and Returning Results**:
   - The valid coupons are sorted first by business line and then by coupon ID.
   - Finally, the function returns a list of valid coupon IDs.

---

## Time and Space Complexity Analysis

### Time Complexity:
- Building the `valid_chars` set involves fixed-time operations for the character ranges, leading to a complexity of O(1) for this setup.
- The main loop processes each of the `n` coupon codes (where `n` is the number of coupons). Each iteration of the loop performs a constant time operation for validation. Thus, the processing of the coupons is O(n).
- The sorting step, which sorts the valid coupons, has a time complexity of O(k log k), where `k` is the number of valid coupons.
- In total, the overall time complexity is \(O(n + k \log k)\).

### Space Complexity:
- The space used to store `valid_chars` is O(1) since it contains a constant number of characters.
- The space required for `valid_businesses` is also O(1) as it contains a fixed set of business types.
- The `valid_coupons` list will take up O(k) space in the worst case (if all coupons are valid).
- Thus, the overall space complexity is \(O(k)\).

---

## Why This Approach is Efficient
1. **Direct Validation**: The method of validating characters against a set is efficient due to average O(1) membership checking. This allows quick validation of characters in each coupon ID.
2. **Clear Structure**: The use of helper functions and clear separation of validation logic (coupon ID and business type) enhances readability and maintainability.
3. **Sorting and Final Output**: Although sorting adds some complexity, it is necessary for ensuring that the final output meets the requirement of being in a specified order, and it does not add significant overhead due to efficient sorting algorithms in Python.
4. **Scalability**: The approach scales linearly with the number of coupons, making it suitable for large datasets without excessive space or time overhead. 

In conclusion, the solution is concise, leverages efficient data structures, and adheres to good programming practices, making it both effective and efficient for the given problem.

Runtime: undefined
Memory: 18032000
"""

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_chars = set(["_"])
        for i in range(ord("a"), ord("z")+1):
            valid_chars.add(chr(i))
        for i in range(ord("A"), ord("Z")+1):
            valid_chars.add(chr(i))
        for i in range(ord("0"), ord("9")+1):
            valid_chars.add(chr(i))

        def is_valid(id):
            if not id: return False
            for el in id:
                if el not in valid_chars:
                    return False
            return True

        valid_businesses = set(["electronics", "grocery", "pharmacy", "restaurant"])
        valid_coupons = []
        for id, business, active in zip(code, businessLine, isActive):
            if is_valid(id) and business in valid_businesses and active:
                valid_coupons.append([id, business, active])

        valid_coupons.sort(key = lambda x: (x[1], x[0]))

        return [x[0] for x in valid_coupons]
