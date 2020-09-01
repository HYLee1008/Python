### Find list of k-closest points to origin using priority queue
###
import heapq


def k_closest(points, K):
    heap = []
    for (x, y) in points:
        dist = x ** 2 + y ** 2
        heapq.heappush(heap, (dist, x, y))

    result = []
    for _ in range(K):
        dist, x, y = heapq.heappop(heap)
        result.append((x, y))
    return result