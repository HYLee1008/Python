### Calculate the time that every node can receive the signal starts from K using Dijkstra algorithm
###
import collections
import heapq

def network_delay_time(times, N, K):
    graph = collections.defaultdict(list)
    # Construct graph
    for u, v, w in times:
        graph[u].append((v, w))

    # Queue: [(time, vertex)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    # Determine the existence of the shortest path
    if len(dist) == N:
        return max(dist.values())
    return -1


print(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))