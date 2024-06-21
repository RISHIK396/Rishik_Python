import numpy as np

def compDegrees(graph):
    num_vertices = len(graph)
    inDegrees = [0] * num_vertices
    outDegrees = [0] * num_vertices

    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                outDegrees[i] += 1
                inDegrees[j] += 1

    return inDegrees, outDegrees


graph= np.array([[0, 1, 0, 1], [1, 0, 0, 1],[1, 1, 0, 1],[1, 1, 1, 0]])


inDegrees, outDegrees = compDegrees(graph)

print("Vertex\tIn-Degree\tOut-Degree")
for i in range(len(graph)):
    print(f"{i}\t{inDegrees[i]}\t\t{outDegrees[i]}")
