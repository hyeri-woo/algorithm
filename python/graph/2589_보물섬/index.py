import sys 
from collections import deque
input = sys.stdin.readline
f = open("test1.txt")
n, m = map(int, f.readline().split())
island = [list(f.readline().strip()) for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(sx, sy, graph):
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and island[nx][ny] == 'L':
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
    return max(max(row) for row in graph)

max_path = 0
for i in range(n):
    for j in range(m):
        if island[i][j] == 'L':
            graph = [[0] * m for _ in range(n)]
            max_path = max(max_path, bfs(i, j, graph))
print(max_path)