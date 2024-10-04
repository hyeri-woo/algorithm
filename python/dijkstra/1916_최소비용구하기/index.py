import sys
import heapq
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [float('inf')] * (n+1)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([w, b])
    # graph[b].append([w, a])

start, end = map(int, input().split())

q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    _w, node = heapq.heappop(q)
    if node == end:
        break
    for weight, next in graph[node]:
        if dist[node] + weight < dist[next]:
            dist[next] = dist[node] + weight
            heapq.heappush(q, [dist[next], next])
print(dist[end])