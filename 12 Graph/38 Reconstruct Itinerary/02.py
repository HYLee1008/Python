### Reconstruct the itinerary starting from JFK using DFS
### Optimized queue operation using stack operation
import collections

def find_itinerary(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []
    def dfs(a):
        route.append(a)
        while graph[a]:
            dfs(graph[a].pop(0))

    dfs('JFK')

    return route


input_1 = [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]
input_2 = [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]

print(find_itinerary(input_1))
print(find_itinerary(input_2))
