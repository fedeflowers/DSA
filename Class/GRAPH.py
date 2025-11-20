# GRAPH

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)  # undirected graph

    def remove_node(self, node):
        if node in self.adj_list:
            # Remove node from its neighbors' lists
            for neighbor in self.adj_list[node]:
                self.adj_list[neighbor].remove(node)
            # Remove the node itself
            del self.adj_list[node]
        else:
            print(f"Node '{node}' not found.")

    def find_node(self, node):
        return node in self.adj_list

    def display(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")
