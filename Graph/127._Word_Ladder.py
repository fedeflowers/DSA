class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Brute Froce
        # res = 0
        # if endWord not in wordList: return res

        # def differ_char(word, wordlist):
        #     res = []
        #     for el in wordlist:
        #         count = 0

        #         for i in range(len(word)):
        #             if word[i] != el[i]:
        #                 count += 1
        #         if count == 1:
        #             res.append(el)
        #     return res

        # start = differ_char(beginWord, wordList)
        # queue = deque([[el, 2] for el in start])
        # visited = set()
        # for el in start:
        #     visited.add(el)
        # while queue:
        #     word, path = queue.popleft()
        #     if word == endWord:
        #         return path

        #     for new_word in differ_char(word, wordList):
        #         if new_word not in visited:
        #             queue.append([new_word, path + 1])
        #             visited.add(new_word)

        # return res

        #Brute Froce
        res = 0
        wordList = set(wordList)
        if endWord not in wordList: return res

        def differ_char(word, wordlist):
            res = []
            for i, ch in enumerate(word):
                start = 'a'
                for alpha in range(ord(start), ord("z")+1):
                    if chr(alpha) != ch:
                        new_word = word[:i] + chr(alpha) + word[i+1:]
                        if new_word in wordList:
                            res.append(new_word)
            return res
        start = differ_char(beginWord, wordList)

        queue = deque([[el, 2] for el in start])
        visited = set()
        for el in start:
            visited.add(el)
        while queue:
            word, path = queue.popleft()
            if word == endWord:
                return path

            for new_word in differ_char(word, wordList):
                if new_word not in visited:
                    queue.append([new_word, path + 1])
                    visited.add(new_word)

        return res



