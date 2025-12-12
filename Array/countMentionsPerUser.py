"""
### Explanation of the Approach

The solution for counting mentions per user in a given event stream is implemented by processing a list of events that indicate when users go online, go offline, or are mentioned. The logic is organized to keep track of a user's online status and their mention counts based on specific event types.

1. **Data Structure Initialization**: 
   - An array `res` is defined to store the counts of mentions for each user indexed by their IDs.
   - A dictionary `ids` is used to keep track of user states, where the key is the user ID, and the value is a tuple containing the online timestamp and the number of mentions.

2. **Sorting Events**: 
   - The events are sorted primarily by timestamp and secondarily by event type (giving precedence to "ONLINE" events using the value of 1 for being online).

3. **Event Processing**:
   - For each event, the code looks at its type (either "OFFLINE", "HERE", "ALL", or mentions for specific users):
     - **OFFLINE**: Updates the user's online timestamp indicating when they went offline.
     - **HERE**: If users are currently online, it increments the mention count for all active users.
     - **ALL**: If all users are there, increment the mention count for every user.
     - **Specific Mentions**: For mentions like "USER1", the code increments the mention count for those specific users.

4. **Final Count Compilation**:
   - After processing all events, the mention counts are compiled back into the `res` array to be returned.

### Time and Space Complexity Analysis

- **Time Complexity**: 
  - Sorting the events takes \(O(E \log E)\) where \(E\) is the number of events, as each event needs to be compared once for sorting.
  - The processing of events is done in \(O(E \times U)\) in the worst case where \(U\) is the number of users, especially when processing through all users for "HERE" or "ALL" events.
  - Thus the overall complexity is \(O(E \log E + E \times U)\).

- **Space Complexity**: 
  - The space used for the `res` array is \(O(U)\) where \(U\) is the number of users.
  - The `ids` dictionary can grow to \(O(U)\) as well, where each user can potentially be a key.
  - Thus, the total space complexity is \(O(U)\).

### Why This Approach is Efficient

1. **Grouped Processing**: 
   - By sorting events and handling bulk operations (like counting mentions for all users or those online) effectively, the solution minimizes the need for repetitive checks.

2. **Direct Mapping**: 
   - Using a dictionary allows for quick updates and retrievals of user states. This direct mapping optimizes the efficiency of state management during event processing.

3. **Scalable**:
   - The code is designed to accommodate a range of events and users, making it suitable for larger datasets, although care must be taken with respect to performance if the number of events or users grows significantly.

Overall, this structured and systematic approach allows the problem to be tackled concisely and efficiently, resulting in manageable time and space complexities.

Runtime: undefined
Memory: 18224000
"""

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        res = [0] * numberOfUsers
        ids = {} # id: [online_timestamp, mentions]
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        def get_users(s):
            new_s = s.split(" ")
            users = [int(i[2:]) for i in new_s]
            return users
        # print(events)
        for typ, timestamp, users in events:
            if typ == 'OFFLINE':
                users = [int(u) for u in users.split(" ")]
                for u in users:
                   _, m = ids.get(u, (0, 0)) 
                   ids[u] = (int(timestamp) +60, m)
            else:
                if users == 'HERE':
                    for u in range(numberOfUsers):
                        t, m = ids.get(u, (0, 0))
                        if t <= int(timestamp):
                            m+=1
                        ids[u] = (t, m)
                elif users == 'ALL':
                    for u in range(numberOfUsers):
                        t, m = ids.get(u, (0, 0))
                        ids[u] = (t, m+1)
                else:
                    users = get_users(users)
                    for u in users:
                        t, m = ids.get(u, (0, 0))
                        # print(u, t, m, timestamp, typ)
                        ids[u] = (t, m+1)
        
        for user in ids:
            res[user] = ids[user][1]
        return res



