import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
        self.edges.append((u, v))

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = 0

        return False

    def graph_coloring(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            print("Solution does not exist")
            return False

        print("Solution exists: Following are the assigned colors")
        for c in color:
            print(c, end=' ')
        self.visualize_graph(color)
        return True

    def visualize_graph(self, color):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        colors = [color[node] for node in G.nodes()]
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, cmap=plt.cm.rainbow)
        plt.show()

def main():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

    m = int(input("Enter the number of colors: "))
    g.graph_coloring(m)

if __name__ == "__main__":
    main()
