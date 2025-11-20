class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #".L.R...LR..L.."
        #"0-101000-1100-100"
        #"0-10211101110"

        #[0, -10, 0, 10, 0, 0, 0, -10, 10, 0, 0, -10, 0, 0]
        #[0, -10, 0, 10, 9, 8, 7, -10, 10, 9, 8, -10, 0, 0] #R to L
        #[-9, -10, 0, 10, 9, (8-8 = 0 arrive at same time), -9, -10, 10, 9 (9-8 = 1 so they stay like this), -9, -10, 0, 0] #L to R
        #[LL.RR.LLRRLL..]

        n = len(dominoes)
        modified_d = []
        for el in dominoes:
            if el == "L":
                modified_d.append(-n)
            elif el == "R":
                modified_d.append(n)
            elif el == '.':
                modified_d.append(0)

        #from right to left
        for i in range(n-1):
            el = modified_d[i]
            next_el = modified_d[i+1]
            if el > 0 and next_el <= 0:
                if (el-1) + next_el > 0:
                    modified_d[i+1] = el-1

        #from left to right
        for i in range(n-1, 0, -1):
            el = modified_d[i]
            next_el = modified_d[i-1]
            if el < 0 and next_el >= 0:
                if (el+1) + next_el < 0:
                    modified_d[i-1] = el+1
                elif (el+1) + next_el == 0:
                    modified_d[i-1] = 0

        #convert
        res = ""
        for el in modified_d:
            if el > 0:
                res += "R"
            elif el < 0:
                res += "L"
            else:
                res += "."

        return res

