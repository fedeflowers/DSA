# ProductOfNumbers

class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.size = 0
            self.stream = [1]
        else:
            self.stream.append(self.stream[self.size]*num)
            self.size += 1
        # print(self.stream)
        

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.stream[self.size] // self.stream[self.size - k ]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)