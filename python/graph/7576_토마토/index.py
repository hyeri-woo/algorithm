from collections import deque
f = open('test5.txt')
n, m = map(int, f.readline().split())
tomatos = [list(map(int, f.readline().split())) for _ in range(m)]

def has_zero(matrix):
    return any(0 in row for row in matrix)

def find_indices_with_value(array, value):
    indices = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                indices.append((i, j))
    return indices

def bfs(graph, visited, start):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x, y in start:
        visited[x][y] = True
    queue = deque([start])
    count = 0
    while queue:
        next_nodes = queue.popleft()
        temp_arr = []
        for x, y in next_nodes:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny] and graph[nx][ny] != -1:
                        temp_arr.append((nx, ny))
                        visited[nx][ny] = True
                        graph[nx][ny] += 1
        if len(temp_arr) > 0:
            queue.append(temp_arr)
            count += 1
    return count


visited = [[False] * n for _ in range(m)]
count = bfs(tomatos, visited, find_indices_with_value(tomatos, 1))
print(-1 if has_zero(tomatos) else count)
