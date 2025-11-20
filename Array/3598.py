# class Solution:
#     def longestCommonPrefix(self, words: List[str]) -> List[int]:
        #brute force
        # def prefix(word1, word2):
        #     i,j = 0,0 
        #     while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
        #         i+=1
        #         j+=1

        #     return max(i,j)


        # def lcp(words):
        #     #get longest common prefix of a list of words count all pairs
        #     res = 0
        #     for i in range(1, len(words)):
        #        res = max(res, prefix(words[i-1], words[i]))

        #     return res

        # res = []
        # for i in range(len(words)):
        #     curr_arr = words[:i] + words[i+1:]
        #     res.append(lcp(curr_arr))
        # return res


        #optimize



class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        N = len(words)

        def lcp(i, j):
            ans = 0
            for a, b in zip(words[i], words[j]):
                if a != b:
                    break
                ans += 1
            return ans

        L = [lcp(i, i + 1) for i in range(N - 1)]
        P = list(accumulate(L, max, initial=0))
        S = list(accumulate(L[::-1], max, initial=0))[::-1]

        ans = [0] * N
        if N == 1:
            return ans
        ans[0] = S[1]
        ans[-1] = P[-2]
        for i in range(1, N - 1):
            ans[i] = max(P[i - 1], S[i + 1], lcp(i - 1, i + 1))
        return ans

        