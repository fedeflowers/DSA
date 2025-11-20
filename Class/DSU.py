# DSU

#UNION BY SIZE
class DSU:
    def __init__(self, els):
        self.parent = {el:el for el in els}
        self.size = {el:1 for el in els}

    def find(self, value):
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])

        return self.parent[value]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return False

        if self.size[parent_a] < self.size[parent_b]:
            self.parent[parent_a] = parent_b
            self.size[parent_b] += self.size[parent_a]
        else:
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]

        return True


# UNION BY RANK (height)
class DSU:
    def __init__(self, elements):
        self.parent = {}
        self.size = {}
        for el in elements:
            self.parent[el] = el
            self.rank[el] = 1

    def find(self, el):
        if el != self.parent[el]:
            self.parent[el] = self.find(self.parent[el])
        return self.parent[el]

    def union(self, a, b):
        p_a = self.find(a)
        p_b = self.find(b)

        if p_a == p_b:
            return False
        if self.rank[p_a] < self.rank[p_b]:
            self.parent[p_a] = p_b
        elif self.rank[p_b] < self.rank[p_a]:
            self.parent[p_b] = p_a
        else:
            self.parent[p_b] = p_a
            self.rank[p_a] += 1

        return True