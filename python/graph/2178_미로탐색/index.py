from collections import deque
f = open('test4.txt', 'r')
n, m = map(int, f.readline().split())
maze = [[int(i) for i in list(f.readline().strip())] for _ in range(n)]

def bfs(graph):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1


bfs(maze)
print(maze[-1][-1])
