# DESIGN_HASHSET

class MyHashSet:

    def __init__(self):
        self.size = 10*3
        self.arr = [None] * self.size
        self.count = 0 #to get resize
        
    def hash_function(self, num):
        return num % self.size
        
    def add(self, key: int) -> None:
        if self.count > self.size * 0.7:
            self.resize()     
        
        index = self.hash_function(key)
        while self.arr[index] != None: 
            if self.arr[index] == key:
                return
            if self.arr[index] == "deleted":
                break
            index = (index + 1) % self.size
            
        self.count += 1
        self.arr[index] = key

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        while self.arr[index] != None: 
            if self.arr[index] == key:
                self.arr[index] = "deleted"
                self.count -= 1
                return
            index = (index + 1) % self.size

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        while self.arr[index] != None: 
            if self.arr[index] == key:
                return True
            index = (index + 1) % self.size
        return False
    
    def resize(self):
        old_arr = self.arr
        self.size = self.size * 2
        self.count = 0
        self.arr = [None] * self.size
        for el in old_arr:
            if el != None and el != "deleted":
                self.add(el)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
#["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]