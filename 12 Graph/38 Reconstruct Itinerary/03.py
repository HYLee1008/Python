### Iterate graph
###
import collections

def find_itinerary(tickets):
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]


input_1 = [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]
input_2 = [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]

print(find_itinerary(input_1))
print(find_itinerary(input_2))