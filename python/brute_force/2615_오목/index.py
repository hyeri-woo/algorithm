import sys
input = sys.stdin.readline
f = open("test1.txt")
n = 19
graph = [list(map(int, f.readline().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
directions = [(0, 1),(1, 0), (1, 1), (-1, 1)]

def is_winning(x, y, color):
    for dx, dy in directions:
        count = 1
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
            count += 1
            if count == 5:
                if 0 <= x - dx < n and 0 <= y - dy < n and graph[x - dx][y - dy] == color:
                    break
                if 0 <= nx + dx < n and 0 <= ny + dy < n and graph[nx + dx][ny + dy] == color:
                    break
                return x, y
            nx += dx
            ny += dy
            
    return None

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            result = is_winning(i, j, graph[i][j])
            if result:
                print(graph[i][j])
                print(result[0] + 1, result[1] + 1)
                sys.exit()
             


print(0)