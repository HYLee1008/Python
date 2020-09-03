### Reconstuct by height using priority queue
###
import heapq


def reconstruction_queue(people):
    heap = []

    for person in people:
        heapq.heappush(heap, (-person[0], [person[1]]))

    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])