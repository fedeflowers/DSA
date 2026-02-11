"""
```markdown
# Explanation of the LeetCode Solution for "Unique Email Addresses"

## 1. Brief Explanation of the Approach

The solution to the problem "Unique Email Addresses" involves normalizing the email addresses according to specific rules and then counting how many unique addresses we get. The main steps in the algorithm are as follows:

- **Splitting the Email**: Each email is split into two parts: the local name and the domain name using the '@' character.
- **Cleaning the Local Name**:
  - The part of the local name before any '+' is considered. Everything after the first '+' is ignored.
  - All '.' characters are removed from the local name.
- **Storing Unique Emails**: The cleaned local name is combined back with the domain name to form the normalized email address, which is then added to a set to ensure uniqueness.
- **Counting Unique Emails**: Finally, the length of the set, which contains all unique normalized emails, is returned.

Here’s how the code executes:
```python
unique_emails = set()  # Initialize an empty set to store unique emails.

for email in emails:
    local, domain = email.split('@')  # Split the email into local and domain parts.
    clean_local = local.split('+')[0].replace('.', '')  # Clean the local part.
    unique_emails.add(clean_local + '@' + domain)  # Add the normalized email to the set.

return len(unique_emails)  # Return the count of unique emails.
```

## 2. Time and Space Complexity Analysis

### Time Complexity
The time complexity is primarily influenced by the number of emails processed and the operations performed on them:

- Let `N` be the number of emails.
- Each email is processed in linear time with respect to its length. Assuming each email has a constant maximum length `L`, the time complexity becomes O(N * L).
- The split, replace, and set operations are efficient, leading to a total time complexity of O(N).

### Space Complexity
The space complexity is determined by the storage of unique email addresses:

- We use a set to store up to `N` unique email addresses in the worst case.
- Hence, the space complexity is O(N).

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Use of Set**: By leveraging a set, we automatically handle duplicates without needing additional logic to check for existent emails. Sets offer average O(1) time complexity for insertions and membership checks.
- **Simplification of Input**: The steps to clean the local name by removing '.' and splitting with '+' focus only on relevant parts, which reduces processing time.
- **Single Pass Processing**: The algorithm processes each email address in a single pass, making the solution optimal with respect to both time and space.
  
In summary, the solution is both time-efficient due to its linear scalability with respect to the number of emails and space-efficient by utilizing a set to maintain uniqueness. Thus, the method effectively meets the problem requirements while maintaining simplicity.
```

Runtime: undefined
Memory: 19468000
"""

# class Solution:
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         res = {}
#         def dedup(email: str):
#             local_name, domain_name = email.split("@")
#             #remove .
#             new_local_name = [c for c in local_name if c != '.']
#             #ignore after +
#             final_local_name = []
#             for c in new_local_name:
#                 if c == '+':
#                     break
#                 final_local_name.append(c)
            
#             return "".join(final_local_name) + "@" + domain_name
            
            
#         for e in emails:
#             res[dedup(e)] = 1
            
#         return len(res)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            # Split by '+' and take the first part, then remove '.'
            clean_local = local.split('+')[0].replace('.', '')
            unique_emails.add(clean_local + '@' + domain)
            
        return len(unique_emails)
