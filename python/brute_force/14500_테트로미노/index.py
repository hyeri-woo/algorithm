import sys 
input = sys.stdin.readline
f = open('test3.txt')
n, m = map(int, f.readline().split())
graph = [list(map(int, f.readline().split())) for _ in range(n)]

# 모든 테트로노미노의 경우의 수
def get_all_tetrominoes():
    tetrominoes = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = [(0, 0)]
    visited = [[False] * 6 for _ in range(6)]
    visited[2][2] = True
    def dfs(sx, sy, count):
        if count == 4:
            tetrominoes.append(result[:])
            return
        for dx, dy in directions:
            x, y = sx + dx, sy + dy
            if not visited[x + 2][y + 2]:
                visited[x + 2][y + 2] = True
                result.append((x, y))
                dfs(x, y, count + 1)
                result.pop()
                visited[x + 2][y + 2] = False
    dfs(0, 0, 1)
    tetrominoes.append([(0, 0), (1, -1), (1, 0), (2, 0)])
    tetrominoes.append([(0, 0), (1, 0), (2, 0), (1, 1)])
    tetrominoes.append([(0, 0), (1, -1), (1, 0), (1, 1)])
    tetrominoes.append([(0, 0), (0, -1), (0, 1), (1, 0)])
    return tetrominoes

# 주어진 포지션에서 주어진 테트로노미노의 합계 계산
def get_tetromino_sum(sx, sy, direction):
    sum = 0
    for dx, dy in direction:
        x, y = sx + dx, sy + dy
        if x < 0 or x >= n or y < 0 or y >= m:
            return -1
        sum += graph[x][y]
    return sum

answer = 0
tetrominoes = get_all_tetrominoes()
for i in range(n):
    for j in range(m):
        for direction in tetrominoes:
            answer = max(answer, get_tetromino_sum(i, j, direction))

print(answer)