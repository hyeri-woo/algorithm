import sys
from collections import deque

input = sys.stdin.readline
f = open('test1.txt')

def bfs(start, group):
    queue = deque([start])
    visited[start] = group
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = -1 * visited[node]
            elif visited[node] == visited[next_node]:
                return False
    return True
        


for _ in range(int(f.readline())):
    v, e = map(int, f.readline().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)

    for _ in range(e):
        a, b = map(int, f.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            is_bipartite = bfs(i, 1)
            if not is_bipartite:
                break
    print('YES' if is_bipartite else 'NO')