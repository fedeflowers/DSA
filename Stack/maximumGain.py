# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         #Brute force
#         res = 0
#         mapping = {"ab": x, "ba": y}
#         start = "ab"
#         end = "ba"
#         if y > x:
#             start = "ba"
#             end = "ab"

#         while s.count(start) >= 1: 
#             res += s.count(start) * mapping[start]
#             s = s.replace(start, "")

#         while s.count(end) >= 1:
#             res += s.count(end) * mapping[end]
#             s = s.replace(end, "")

#         return res

        #optimized

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def how_many(s, include, to_pop):
            s = list(s)
            idx_to_del = set()
            stack = []
            new_s = []
            res = 0
            for i, el in enumerate(s):
                if el == include:
                    stack.append((i, el))
                elif stack and el == to_pop:
                    idx, _ = stack.pop()
                    idx_to_del.add(idx)
                    idx_to_del.add(i)
                    res += 1
                elif stack and el != to_pop:
                    stack = []
            for i, el in enumerate(s):
                if i in idx_to_del:
                    continue
                new_s.append(el)
            new_s = "".join(new_s)
            return new_s, res

        res = 0
        if x > y: #ab -> ba
            new_s, tot = how_many(s, "a", "b")
            res += tot * x
            new_s, tot = how_many(new_s, "b", "a")
            res += tot * y
            
        elif y > x: #ba -> ab
            new_s, tot = how_many(s, "b", "a")
            res += tot * y
            new_s, tot = how_many(new_s, "a", "b")
            res += tot * x

        else: #ab -> ba, ba -> ab
            new_s, tot = how_many(s, "a", "b")
            res += tot * x
            new_s, tot = how_many(new_s, "b", "a")
            res += tot * y

            res2 = 0
            new_s, tot = how_many(s, "b", "a")
            res2 += tot * y
            new_s, tot = how_many(new_s, "a", "b")
            res2 += tot * x
            return max(res, res2)


        #se valgono uguale provo prima ab e poi ba come start

        #maybe with stack ? like b,b, a = pop, a = pop etc.. and i create all ba, but how to remove efficiently?
        #keep track of removed indices, aka the ones removed from word and from stack
        

        return res
    

#BEST one:
# the stack will contain the word without the removed characters if I add all elements, and i dont need to do ab -> ba and ba -> ab if x == y
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s: str, first: str, second: str, val: int):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += val
                else:
                    stack.append(c)
            return "".join(stack), score

        if x >= y:
            s, score1 = remove_pattern(s, 'a', 'b', x)
            _, score2 = remove_pattern(s, 'b', 'a', y)
        else:
            s, score1 = remove_pattern(s, 'b', 'a', y)
            _, score2 = remove_pattern(s, 'a', 'b', x)

        return score1 + score2

