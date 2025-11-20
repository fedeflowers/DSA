# DESIGN_HASHMAP

class MyHashMap:
    DELETED = object()              # a unique sentinel (safer than the string "deleted")

    def __init__(self):
        self.size   = 10 ** 3
        self.keys   = [None] * self.size
        self.values = [None] * self.size
        self.count  = 0

    def hash_function(self, num):
        return num % self.size

    def put(self, key: int, value: int) -> None:
        # grow when the real load factor (excluding DELETED) exceeds 0.7
        if self.count > 0.7 * self.size:
            self.resize()

        idx = self.hash_function(key)
        first_deleted  = -1                         # remember the first DELETED spot
        while self.keys[idx] is not None:
            if self.keys[idx] == key:               # key already present → update
                self.values[idx] = value
                return
            if self.keys[idx] is MyHashMap.DELETED and first_deleted == -1:
                first_deleted = idx                 # mark slot but keep searching
            idx = (idx + 1) % self.size

        # key not found → insert
        insert_idx = first_deleted if first_deleted != -1 else idx
        self.keys[insert_idx]   = key
        self.values[insert_idx] = value
        self.count += 1

    def get(self, key: int) -> int:
        idx = self.hash_function(key)
        while self.keys[idx] is not None:
            if self.keys[idx] is not MyHashMap.DELETED and self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
        return -1

    def remove(self, key: int) -> None:
        idx = self.hash_function(key)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx]   = MyHashMap.DELETED
                self.values[idx] = None             # optional: free the value slot
                self.count      -= 1
                return
            idx = (idx + 1) % self.size

    def resize(self) -> None:
        old_keys, old_values = self.keys, self.values
        self.size  *= 2
        self.keys   = [None] * self.size
        self.values = [None] * self.size
        self.count  = 0
        for k, v in zip(old_keys, old_values):
            if k not in (None, MyHashMap.DELETED):
                self.put(k, v)
