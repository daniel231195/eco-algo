color = {}
prev = {}
vertex = []
edge = {}

def init_graph(matrix):
    """
        we build graph and after that we use in dfs to find if have cycle in graph
    :param matrix: matrix of graph
    :return: if in graph have cycle
    """
    global vertex
    global edge
    for i in range(0, len(matrix) + len(matrix[0])):
        vertex.append(i)
        edge[i] = []
    for i in range(0, len(matrix)):
        edge[i] = []
        for j in range(0, len(matrix[0])):
            if matrix[i][j] > 0:
                edge[i].append(len(matrix) + j)
                edge[len(matrix) + j].append(i)
    for i in range(0, len(vertex)):
        color[i] = 'white'
        prev[i] = -1
    print(vertex) # vertex of graph
    print(edge) # the edge of the graph
    ans = False
    for i in range(0, len(vertex)):
        if ans is False and color[i] == 'white':
            ans = dfs_visit(i)
    if ans is False:
        return 'No cycle in graph'
    else:
        return 'Have cycle in graph'


def dfs_visit(u):
    """
        use in dfs algorithm  to find if have cycle in graph
    :param u: vertex of start
    :return: rerun ture if in the graph have cycle else no cycle is false
    """
    ans = False
    color[u] = 'gray'
    for v in edge[u]:
        if ans is False:
            if color[v] == 'gray':
                if prev[u] is not v:
                    ans = True
            elif color[v] == 'white':
                prev[v] = u
                ans = dfs_visit(v)
    color[u] = 'black'
    return ans


if __name__ == '__main__':
    # init_graph([[1, 1, 0.07, 0], [0, 0, 0.93, 1]])
    print(init_graph([[1, 1, 0.07, 0], [0, 0, 0.93, 1]]))
