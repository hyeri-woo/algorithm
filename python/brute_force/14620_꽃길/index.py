import sys
from itertools import combinations
f = open('test1.txt')
input = sys.stdin.readline
n = int(f.readline())
graph = [list(map(int, f.readline().split())) for _ in range(n)]


# 꽃을 심을 때 각 위치에서의 비용을 계산하기 위한 방향들
flower_directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

# 특정 위치에 꽃을 심었을 때의 비용 계산
def calculate_cost(x, y):
    total_cost = 0
    for dx, dy in flower_directions:
        nx, ny = x + dx, y + dy
        total_cost += graph[nx][ny]
    return total_cost

# 특정 위치에 꽃을 심을 수 있는지 확인
def can_place(x, y, visited):
    for dx, dy in flower_directions:
        nx, ny = x + dx, y + dy
        if visited[nx][ny]:
            return False
    return True

# 특정 위치에 꽃을 심었을 때 방문 처리
def place_flower(x, y, visited):
    for dx, dy in flower_directions:
        nx, ny = x + dx, y + dy
        visited[nx][ny] = True

# 모든 가능한 위치에서 꽃을 심는 경우를 고려하여 최소 비용 계산
def get_min_cost():
    positions = [(i, j) for i in range(1, n - 1) for j in range(1, n - 1)]
    min_cost = sys.maxsize

    for comb in combinations(positions, 3):
        visited = [[False] * n for _ in range(n)]
        valid = True
        total_cost = 0

        for x, y in comb:
            if can_place(x, y, visited):
                total_cost += calculate_cost(x, y)
                place_flower(x, y, visited)
            else:
                valid = False
                break

        if valid:
            min_cost = min(min_cost, total_cost)

    return min_cost

# 결과 출력
print(get_min_cost())