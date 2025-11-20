class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        #computo da sx a dx e da dx a sx così posso farlo in tempo n,
        #ogni volta aggiungo il numero di palle perchè per andare da una posizione ad una adiacente mi basta
        #computare il numero di palle e aggiungerle perchè devo spostare ogni volta tot palle per inserle nel box i
        l_r = [0] * n
        r_l = [0] * n

        tot_balls = 0
        tot_operations = 0
        for i in range(n):
            tot_operations += tot_balls
            l_r[i] = tot_operations
            if boxes[i] == '1':
                tot_balls += 1

        tot_balls = 0
        tot_operations = 0
        for i in reversed(range(n)):
            tot_operations += tot_balls
            r_l[i] = tot_operations
            if boxes[i] == '1':
                tot_balls += 1

        for i in range(n):
            l_r[i] += r_l[i]
        return l_r