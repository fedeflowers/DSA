class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #0 sta dov'è, -num vai indietro e +num vai inavanti
        arr_diff = [0] * (len(s)+1)
        final_shifts = []
        for shift in shifts:
            if shift[2]:
                arr_diff[shift[0]] += 1
                arr_diff[shift[1]+1] -= 1
            else:
                arr_diff[shift[0]] -= 1
                arr_diff[shift[1]+1] += 1

        shift = 0
        for i in range(len(arr_diff)-1):
            shift += arr_diff[i]
            final_shifts.append(shift)

        res = ""
        for i, el in enumerate(final_shifts):
            new_char = chr((ord(s[i]) - ord('a') + el) % 26 + ord('a'))
            res += new_char
        return res
