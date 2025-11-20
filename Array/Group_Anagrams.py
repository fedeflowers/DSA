# Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())