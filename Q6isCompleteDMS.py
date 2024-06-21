import numpy as np



def isComplete(adjMat):
    num_vertices = len(adjMat)

    # Check if the number of edges is equal to the maximum possible number of edges
    max_edges = (num_vertices * (num_vertices - 1)) // 2
    num_edges = sum(adjMat[i][j] for i in range(num_vertices) for j in range(i + 1, num_vertices))
    if num_edges != max_edges:
        return False

    # Check if there are no self-loops (diagonal elements) and no missing edges
    for i in range(num_vertices):
        if adjMat[i][i] != 0:
            return False
        for j in range(i + 1, num_vertices):
            if adjMat[i][j] != 1 or adjMat[j][i] != 1:
                return False

    return True


#graphMat= np.array([[1,0,1],[0,1,1],[0,0,0]])
#graphMat= np.array([[0, 1, 1, 0], [1, 0, 1, 1],[1, 1, 0, 1],[0, 1, 1, 0]])
#graphMat= np.array([[0, 1, 1, 1], [1, 0, 1, 1],[1, 1, 0, 1],[1, 1, 1, 0]])

print(isComplete(graphMat))
