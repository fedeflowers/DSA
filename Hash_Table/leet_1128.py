class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # #brute force
        # res = 0

        # n = len(dominoes)
        # for i in range(n):
        #     a, b = dominoes[i][0], dominoes[i][1]
        #     for j in range(i+1, n):
        #         c, d = dominoes[j][0], dominoes[j][1]
        #         if (a == c and b==d )or (a==d and b==c):
        #             res += 1

        # return res 

        # optimized
        # {(1,2):3, (1,1):1, (2,2):1}
        d = {}
        res = 0

        for domino in dominoes:
            domino.sort()
            d[tuple(domino)] = d.get(tuple(domino), 0) + 1
        for _, val in d.items():
            if val > 1:
                res += (val*(val-1))//2 

        return res


        # el 2 : 1 pair
        # el 3 : 3 pair
        # el 4 : 6 pair
        # el 5 : 10 pair
        #for each el add n-1

        # 1 + 2 + 3 + 4

        # 5 = n(n-1)//2
        # 5*4//2