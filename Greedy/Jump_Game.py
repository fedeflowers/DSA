# Problem: Jump Game
# Link: https://leetcode.com/problems/jump-game/

def canJump(nums):
    furthest = 0
    for i, jump in enumerate(nums):
        if i > furthest:
            return False
        furthest = max(furthest, i + jump)
    return True