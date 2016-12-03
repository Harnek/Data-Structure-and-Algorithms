'''
author : https://github.com/Harnek
Floyd–Warshall algorithm - All-pairs shortest path problem (for weighted graphs)

Complexity: 
Performance = |V|^3
Space       = |V|^2
'''

def allPairsShortestPath(graph):
    
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = float('inf')
            pred[u][v] = None

        dist[u][u] = 0
        pred[u][v] = None

        for v in graph[u]:
            dist[u][v] = graph[u][v]
            pred[u][v] = u

    #[print(dist[v]) for v in dist]

    for mid in graph:
        for u in graph:
            for v in graph:
                newLen = dist[u][mid] + dist[mid][v]
                if newLen < dist[u][v]:
                    dist[u][v] = newLen
                    pred[u][v] = pred[mid][v]

    return dist, pred

graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}

dist, pred = allPairsShortestPath(graph)

for v in dist:
    print(v, dist[v])
