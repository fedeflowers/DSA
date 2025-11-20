class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        done = {}
        res = []
        tmp = 0
        for key, color in queries:
            if key in done:
                old_color = done[key]
                colors[old_color] -= 1
                if colors[old_color] <= 0 :
                    tmp -= 1
            
            if colors[color] == 0:#its default dict so if it's 0 it's never encounterd before or again to add to distinct colors
                tmp +=1
            colors[color] += 1
            done[key] = color
            
            res.append(tmp)
        return res