class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diff_indices = []
        for i in range(n):
            if s1[i] != s2[i]:
                diff_indices.append(i)

        if len(diff_indices) == 0:
            return True
        elif len(diff_indices) == 2:
            if (s1[diff_indices[1]] == s2[diff_indices[0]] 
                and s1[diff_indices[0]] == s2[diff_indices[1]]):
                return True
            else:
                return False    
        else:
            return False