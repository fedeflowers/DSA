# BFS_graph_traversal_and_in_degree

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #io farei  edges al contrario, quindi parto dai nodi terminali, vedo dove finiscono, se finiscono in nodo che ha come entrata un path da un nodo terminale e basta allora viene aggiunto anche quello alla risposta, altrimenti no. così dovrebbe bastare una sola visita del grafo invece che fare una visita per nodo.
        #use in-degree to find how many edges are going in


        reversed_adj_list = defaultdict(list)
        in_degree = {}
        res = []
        queue = deque()
        n = len(graph)
        for i in range(n):
            for el in graph[i]:
                reversed_adj_list[el].append(i) 
            if len(graph[i]) == 0:
                queue.append(i)
                in_degree[i] = 0
            else:
                in_degree[i] = len(graph[i])

        while queue:
            el = queue.popleft()
            res.append(el)
            for neighbour in reversed_adj_list[el]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        res.sort()
        return res

