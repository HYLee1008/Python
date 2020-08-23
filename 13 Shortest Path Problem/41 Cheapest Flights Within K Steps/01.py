### Find cheapest flights within k steps using dijkstra algorithm
###
import collections
import heapq

def find_cheapest_price(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    # Construct graph
    for u, v, w in flights:
        graph[u].append((v, w))

    # Queue: [(price, vertex, left steps)]
    Q = [(0, src, K)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1


print(find_cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
