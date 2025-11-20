class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #sliding window, take k elements and keep the one with the lowest whites, n* of whites = result

        whites = sum(1 for i in range(k) if blocks[i] == 'W') 
        min_whites = whites
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W': 
                whites -= 1
            if blocks[i] == 'W': 
                whites += 1
            min_whites = min(min_whites, whites)
        
        return min_whites
