class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = 0
        res = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                i+=1
            j+=1
        return res
