'''
author : https://github.com/Harnek
Prim's algorithm is a minimum-spanning-tree algorithm (for weighted undirected graph)

Complexity: 
Performance::
    Adjacency matrix = O(|V|^2)
    Adjacency list with heap = O(|E| log|V|)
'''

def prim(s, edges, n):
    wt = 0
    V = set(range(1,n+1))
    A = set()
    A.add(s)
    while A != V:
        for e in edges:
            if (e[0] in A and e[1] in V-A) or (e[1] in A and e[0] in V-A):
                A.add(e[0])
                A.add(e[1])
                wt += e[2]
                edges.remove(e)
                break
    return wt

# n = no of vertices
n = 4

edges = [[1, 2, 1],
         [4, 3, 99],
         [1, 4, 100],
         [3, 2, 150],
         [3, 1, 200]]

edges.sort(key=lambda l: l[2])

print(prim(1, edges, n))