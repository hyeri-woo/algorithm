# import sys
# input = sys.stdin.readline
from collections import deque
f = open("test1.txt")
input = f.readline
m, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]

answer = float('inf')

def bfs(start):
    visited = [[0] * n for _ in range(m)]
    dist = [[0] * n for _ in range(m)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    maxi =  -1 * float('inf')
    while len(q) > 0:
        ey, ex = q.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = ey + dy, ex + dx
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] == 'L':
                if visited[ny][nx] > 0:
                    continue
                
                visited[ny][nx] = 1
                dist[ny][nx] = dist[ey][ex] + 1
                maxi = max(maxi, dist[ny][nx])
                q.append((ny, nx))
    return maxi

answer = -1 * float('inf')
for j in range(m):
    for i in range(n):
        if graph[j][i] == 'L':
            answer = max(answer, bfs((j, i)))

print(answer)