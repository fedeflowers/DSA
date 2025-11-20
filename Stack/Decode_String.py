# Problem: Decode String
# Link: https://leetcode.com/problems/decode-string/

def decodeString(s):
    num_stack = []
    str_stack = []
    current_str = ""
    current_num = 0

    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == '[':
            num_stack.append(current_num)
            str_stack.append(current_str)
            current_num = 0
            current_str = ""
        elif ch == ']':
            repeat = num_stack.pop()
            prev = str_stack.pop()
            current_str = prev + current_str * repeat
        else:
            current_str += ch

    return current_str