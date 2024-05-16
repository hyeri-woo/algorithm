import sys
input = sys.stdin.readline
f = open("test5.txt")
n, m = map(int, f.readline().split())
graph = [list(f.readline().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
is_cycle = False

def dfs(color, x, y, sx, sy, cnt):
    global is_cycle
    if is_cycle:
        return
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if cnt >= 4 and nx == sx and ny == sy:
            is_cycle = True
            return
        if not visited[nx][ny] and graph[nx][ny] == color:
            visited[x][y] = True
            dfs(color, nx, ny, sx, sy, cnt+1)
            visited[x][y] = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(graph[i][j], i, j, i, j, 1)

print("Yes" if is_cycle else "No")

    
