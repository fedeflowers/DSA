class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        #extend array
        for i in range(k-1):
            colors.append(colors[i])
        n = len(colors)
        start = 0
        res = 0
        end = 1
        while end < n:
            if colors[end-1] == colors[end]: #not alternating
                start = end #reset window
            
            if end - start +1 == k:
                res+= 1
                start += 1
            end += 1

        return res
