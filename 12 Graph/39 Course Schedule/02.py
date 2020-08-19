### Determine whether given n course can be completed or not using pruning
### Add visited set to prevent redundant graph search. 10 Times faster than DFS.
import collections

def can_finish(numCourse, prerequisites):
    graph = collections.defaultdict(list)
    # Construct graph
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # False if graph is cyclic
        if i in traced:
            return False
        # True if node is visited
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # Remove node after search
        traced.remove(i)
        # Add visited node after search
        visited.add(i)

        return True

    # Determine
    for x in list(graph):
        if not dfs(x):
            return False

    return True


print(can_finish(2, [[1, 0]]))
print(can_finish(2, [[1, 0], [0, 1]]))
print(can_finish(2, [[1, 0], [2, 0], [2, 3]]))