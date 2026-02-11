"""
## Explanation of the Solution for "Unique Email Addresses"

### 1. Brief Explanation of the Approach

The solution aims to determine the number of unique email addresses based on specific rules governing the format of the email. Each email has a local name and a domain name separated by an '@' symbol. The rules for uniqueness consider the following:

- Dots ('.') in the local name are ignored. For example, "test.email" and "testemail" are treated as the same.
- Any characters after the first '+' in the local name are disregarded. For instance, "test.email+alex" is equivalent to "test.email".

To achieve this, the `dedup` function processes each email:
- It splits the email into local and domain parts.
- It removes all dots from the local name and stops processing the local name when the first '+' is encountered.
- The cleaned-up local name is then combined with the domain name to construct a normalized email address.
  
The function then uses a dictionary to collect unique normalized emails (using the email as a key) and counts them.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N * M)
  - N is the number of emails. For each email, we process it in linear time relative to its length M. Each email requires splitting, cleaning of the local name, and concatenation with the domain part.

- **Space Complexity**: O(K)
  - K is the number of unique emails stored in the dictionary. In the worst case, if all emails are unique after normalization, we store each email in the dictionary, leading to O(K) space usage.

### 3. Why This Approach is Efficient

The method leverages Python's dictionary to ensure that only unique email addresses are counted efficiently. By storing normalized email addresses, it avoids duplicates effortlessly since dictionary keys are unique by nature. The performance is optimized by working directly with string operations on each email only once, ensuring the transformation is linear relative to the input size, and thus scalable for larger datasets. The overall approach is straightforward and clear, allowing for easy understanding and maintenance while effectively handling the problem constraints.

Runtime: undefined
Memory: 19400000
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = {}
        def dedup(email: str):
            local_name, domain_name = email.split("@")
            #remove .
            new_local_name = [c for c in local_name if c != '.']
            #ignore after +
            final_local_name = []
            for c in new_local_name:
                if c == '+':
                    break
                final_local_name.append(c)
            
            return "".join(final_local_name) + "@" + domain_name
            
            
        for e in emails:
            res[dedup(e)] = 1
            
        return len(res)
