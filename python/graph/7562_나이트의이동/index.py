from collections import deque
f = open('test1.txt')
cases = int(f.readline())

def bfs(graph, n, start, end):
    directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    visited = [[False] * n for _ in range(n)]
    sx, sy = start
    visited[sx][sy] = True
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1

for _ in range(cases):
    n = int(f.readline())
    start = list(map(int, f.readline().split()))
    end = list(map(int, f.readline().split()))
    graph = [[0] * n for _ in range(n)]
    bfs(graph, n, start, end)
    print(graph[end[0]][end[1]])