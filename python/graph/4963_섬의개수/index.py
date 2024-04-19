import sys
sys.setrecursionlimit(10**6)
f = open('test1.txt')
w, h = -1, -1

def dfs(graph, x, y, visited):
    visited[x][y] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(graph, nx, ny, visited)

while w != 0 or h != 0:
    w, h = map(int, f.readline().split())
    if w == 0 or h == 0:
        break
    data = [list(map(int, f.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and data[i][j] == 1:
                dfs(data, i, j, visited)
                count += 1

    print(count)