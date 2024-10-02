# import sys
# input = sys.stdin.readline
import heapq
from collections import deque
f = open("test1.txt")
input = f.readline

n, m = map(int, input().split())
s = int(input())
links = [[] for _ in range(n+1)]
dist = [float('inf')] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    links[a].append([b, c])

q = []
heapq.heappush(q, [0, s])
dist[s] = 0

while q:
    # 우선순위 큐를 이용해서, 거리를 보고 정렬한다
    _w, node = heapq.heappop(q)
    for next, weight in links[node]:
        # 1. 각각의 노드에 값을 업데이트
        # 2. 여러 경로가 있다면 min 비교
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탐색
        if dist[node] + weight  < dist[next]:
            dist[next] = dist[node] + weight
            heapq.heappush(q, [dist[next], next])

for i in range(1, n+1):
    if dist[i] >= float('inf'):
        print("INF")
    else:
        print(dist[i])