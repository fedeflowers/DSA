"""
# Explanation of the LeetCode Solution for "Count Mentions Per User"

## 1. A Brief Explanation of the Approach

The solution employs a straightforward simulation of user activities based on a list of events. The key steps involved are as follows:

- **Initialization**: 
  - A list, `res`, is created to hold the mention counts for each user, initialized to zero.
  - A dictionary, `ids`, is used to associate each user ID with a tuple containing their online timestamp and the count of mentions.

- **Sorting Events**: 
  - The events list is sorted by timestamp and type (online events prioritized over offline events if they occur at the same time).

- **Event Processing**:
  - Each event is processed in order:
    - For **OFFLINE** events, the user is marked as online for an additional 60 seconds, allowing mentions during this window to be counted.
    - For **HERE** events, every user has their mention count incremented if they have been online until the timestamp of the event.
    - For **ALL** events, each user’s mention count is incremented regardless of their current online status.
    - For specific user mentions, the respective user IDs are extracted, and their mention counts are incremented.

- **Final Count Retrieval**: 
  - After processing all events, the mention counts from `ids` are transferred to the result list `res`, which is then returned.

## 2. Time and Space Complexity Analysis

- **Time Complexity**:
  - Sorting the events takes \(O(E \log E)\), where \(E\) is the number of events.
  - Processing each event takes \(O(E \cdot U)\) where \(U\) is the number of users (in the worst case, loop through all users).
  - Thus, the combined time complexity is \(O(E \log E + E \cdot U)\).

- **Space Complexity**:
  - The space complexity is dominated by the `ids` dictionary which stores information for up to \(U\) users in the worst case, i.e., \(O(U)\).
  - The results list `res` also takes \(O(U)\).

Therefore, the overall space complexity is \(O(U)\).

## 3. Why this Approach is Efficient

This approach is efficient for a few reasons:

- **Sorting**: By sorting the events by timestamp, the solution ensures that all time-sensitive operations (like checking if the user was online) are handled correctly.
- **Dictionary for User States**: The use of a dictionary allows for efficient retrieval and updating of user states (online status and mention counts).
- **Simplicity**: The logic is straightforward and relies on a clear and systematic processing of events, avoiding unnecessary complexity.

Overall, this solution is both clear and efficient, making it suitable for handling potentially large inputs with many users and events while ensuring accurate mention counts.

Runtime: N/A
Memory: N/A
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



