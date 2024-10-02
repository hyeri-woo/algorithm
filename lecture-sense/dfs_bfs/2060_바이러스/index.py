# import sys
# input = sys.stdin.readline
from collections import deque
f = open("test1.txt")
input = f.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n + 1)]

# dfs
# def recur(node):
#     visited[node] = 1
#     for next in graph[node]:
#         if visited[next] == 1:
#             continue
#         recur(next)

# recur(1)

# print(sum(visited) - 1)

q = deque()

q.append(1)

while len(q) > 0:
    node = q.popleft()
    visited[node] = 1
    for next in graph[node]:
        if visited[next] == 1:
            continue
        q.append(next)

print(sum(visited) - 1)