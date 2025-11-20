class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = right = 0
        count = {}
        res = 0

        while right < n:
            count[s[right]] = count.get(s[right], 0) + 1

            while len(count) == 3:
                res += n - right
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left +=1

            right += 1

        return res

        