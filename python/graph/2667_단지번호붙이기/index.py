import sys
sys.setrecursionlimit(10**6)
f = open('test1.txt')
n = int(f.readline())
graph = [[int(i) for i in list(f.readline().strip())] for _ in range(n)]

def dfs(graph, x, y, visited):
    visited[x][y] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(graph, nx, ny, visited)

visited = [[False] * n for _ in range(n)]
count = 0
houses = []
prevCount = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(graph, i, j, visited)
            count += 1
            sumTrue = sum(row.count(True) for row in visited)
            houses.append(sumTrue - prevCount)
            prevCount = sumTrue
        
print(count)
print('\n'.join(map(str, sorted(houses))))