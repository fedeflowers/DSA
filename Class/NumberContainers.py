# NumberContainers

class NumberContainers:

    def __init__(self):
        self.index_to_num = defaultdict(int)
        self.num_to_min = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        old_num = self.index_to_num[index]
        self.index_to_num[index] = number
        try:
            self.num_to_min[old_num].remove(index)
        except:
            pass
        #add in sorted arr
        bisect.insort(self.num_to_min[number], index)

    def find(self, number: int) -> int:
        if number in self.num_to_min and len(self.num_to_min[number]) >= 1:
            return self.num_to_min[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)