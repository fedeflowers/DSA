class Solution:
    # def maximumSwap(self, num: int) -> int:
        #brute force
        # str_num = str(num)
        # arr_num = list(str_num)

        # n = len(arr_num)
        # res = num

        # for i in range(n):
        #     for j in range(i+1, n):
        #         arr_num[i], arr_num[j] = arr_num[j], arr_num[i]
        #         res = max(res, int("".join(arr_num)))
        #         arr_num[i], arr_num[j] = arr_num[j], arr_num[i]

        # return res


    #O(N) one pass
    def maximumSwap(self, num):
        arr_num = list(str(num))
        n = len(arr_num)

        last_idx_num = [None] * 10

        for i, el in enumerate(arr_num):
            last_idx_num[int(el)] = i #update last idx for el

        for i, el in enumerate(arr_num):
            # swap if there is a bigger num after the current one (biggest number)
            for j in range(9, int(el), -1): # this way starts from 9 and go until el
                if last_idx_num[j] and last_idx_num[j] > i:
                    #swap
                    arr_num[i], arr_num[last_idx_num[j]] = arr_num[last_idx_num[j]], arr_num[i]
                    return int("".join(arr_num))

        return num
