"""
Find a Mother Vertex in a Graph
What is a Mother Vertex?
A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.
"""

class Graph:
    def __init__(self, nodes):
        self.graph= {}
        self.nodes= nodes

    def add_edge(self, edge):
        if edge[0] not in self.graph:
            self.graph[edge[0]]= set()
        self.graph[edge[0]].add(edge[1])

    def dfs(self, u, visited):
        visited.add(u)
        if u not in self.graph:
            return
        for v in self.graph[u]:
            if v not in visited:
                self.dfs(v, visited)

    def find_mother(self):
        visited= set()
        v=0
        for node in range(self.nodes):
            if node not in visited:
                self.dfs(node, visited)
                v= node
        visited= set()
        self.dfs(v, visited)
        if len(visited)==self.nodes:
            return v
        return -1


def main():
    g= Graph(7)
    g.add_edge([0,1])
    g.add_edge([0,2])
    g.add_edge([1,3])
    g.add_edge([4,1])
    g.add_edge([6,4])
    g.add_edge([5,6])
    g.add_edge([5,2])
    g.add_edge([6,0])

    print g.find_mother()


if __name__ == '__main__':
    main()
