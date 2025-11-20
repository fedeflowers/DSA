# leetcode_332

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(node):
            while adj[node]:
                next_dest = heapq.heappop(adj[node])
                dfs(next_dest)
            res.append(node)

        dfs("JFK")
        return res[::-1]  # reverse because we build post-order
