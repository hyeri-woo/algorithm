import sys
from collections import deque
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
l, r, c = map(int, input().split())

# 건물의 grid를 구하는 함수
def get_building_grid():
    building = []
    for _ in range(l):
        layer = []
        for _ in range(r):
            layer.append(list(input().strip()))
        building.append(layer)
        input()
    return building

# 시작점과 출구를 반환하는 함수
def get_start_goal(l, r, c, building):
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if building[z][y][x] == 'S':
                    start = (x, y, z)
                elif building[z][y][x] == 'E':
                    end = (x, y, z)
    return start, end

# 너비 우선 탐색으로 출구까지 몇분이 걸리는지 찾거나, 탈출하지 못하는 것을 반환
def bfs(l, r, c, start, end, building):
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    sx, sy, sz = start
    ex, ey, ez = end
    building[sz][sy][sx] = 0
    visited[sz][sy][sx] = True
    queue = deque([start])
   
    while queue:
        x, y, z = queue.popleft()
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or nx >= c or ny < 0 or ny >= r or nz < 0 or nz >= l:
                continue
            if not visited[nz][ny][nx] and building[nz][ny][nx] == '.':
                queue.append((nx, ny, nz))
                visited[nz][ny][nx] = True
                building[nz][ny][nx] = building[z][y][x] + 1
            if not visited[nz][ny][nx] and building[nz][ny][nx] == 'E':
                building[nz][ny][nx] = building[z][y][x] + 1
    return building[ez][ey][ex]
            

while l != 0 and r != 0 and c != 0:
    building = get_building_grid()
    start, end = get_start_goal(l, r, c, building)
    result = bfs(l, r, c, start, end, building)
    if result == 'E':
        print('Trapped!')
    else:
        print(f"Escaped in {result} minute(s).")
    l, r, c = map(int, input().split())
