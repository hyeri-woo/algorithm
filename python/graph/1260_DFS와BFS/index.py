from collections import deque
f = open("test3.txt", "r")
n, m, v = map(int, f.readline().split())
data = [list(map(int, f.readline().split())) for _ in range(m)]
graph = {}
for start, end in data:
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]
    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

for node, edges in graph.items():
    graph[node] = sorted(edges)

def dfs(graph, start):
    checked = []
    will_check = [start]
    while will_check:
        node = will_check.pop()
        if node not in checked:
            checked.append(node)
            if node in graph:
                will_check.extend(reversed(graph[node]))
    return checked

def bfs(graph, start):
    checked = []
    will_check = deque()
    will_check.append(start)
    while will_check:
        node = will_check.popleft()
        if node not in checked:
            checked.append(node)
            if node in graph:
                will_check.extend(graph[node])
    return checked

print(' '.join(map(str, dfs(graph, v))))
print(' '.join(map(str, bfs(graph, v))))