class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def isSafe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graphColorUtil(self, m, color, v):
        if v == self.V:
            return True
        for c in range(1, m+1):
            if self.isSafe(v, color, c) == True:
                color[v] = c
                if self.graphColorUtil(m, color, v+1) == True:
                    return True
                color[v] = 0

    def graphColoring(self, m):
        color = [0] * self.V
        if self.graphColorUtil(m, color, 0) == False:
            return False
        return color

if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]

    color = g.graphColoring(2)
    if color != False:
        print(color)
    else:
        print("Graph cannot be colored with 2 colors")
