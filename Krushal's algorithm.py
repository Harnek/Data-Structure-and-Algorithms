'''
author : https://github.com/Harnek
Kruskal's algorithm is a minimum-spanning-tree algorithm (for weighted undirected graph)

Pseudocode
------------------------------------------------------------
KRUSKAL(G):
1 A = ∅
2 foreach v ∈ G.V:
3    MAKE-SET(v)
4 foreach (u, v) in G.E ordered by weight(u, v), increasing:
5    if FIND-SET(u) ≠ FIND-SET(v):
6       A = A ∪ {(u, v)}
7       UNION(u, v)
8 return 
------------------------------------------------------------

Complexity: 
Performance = O(|E| log|E|) or O(|E| log|V|)
'''

def find(e, l):
    for i in l:
        if e[0] in i and e[1] in i:
            return 0
    return 1
    
def union(e, l):
    for i in range(len(l)):
        if e[0] in l[i]:
            t1 = l.pop(i)
            break
    for i in range(len(l)):
        if e[1] in l[i]:
            t2 = l.pop(i)
            break
    l.append(t1|t2)
    return l

def krushal(s, edges, l):
    wt = 0
    for e in edges:
        if len(l) > 1:
            if find(e, l):
                wt += e[2]
                l = union(e, l)
        else:
            return wt      
    return wt

# n = no of vertices
n = 4

edges = [[1, 2, 1],
         [4, 3, 99],
         [1, 4, 100],
         [3, 2, 150],
         [3, 1, 200]]

edges.sort(key=lambda l: l[2])

#l is list of set for every vertices
l = [{1}, {2}, {3}, {4}]

print(krushal(1, edges, l))