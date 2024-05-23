import sys
from itertools import combinations
input = sys.stdin.readline
f = open('test4.txt')
n, m = map(int, f.readline().split())
graph = [list(map(int, f.readline().split())) for _ in range(n)]
position_house = []
position_chicken = []

# 모든 집에서 치킨 집 중 가장 가까운 거리 계산
def calculate_sum_distance(selected_chicken):
    sum_distance = 0
    for house in position_house:
        x, y = house
        min_distance = sys.maxsize
        for i, j in selected_chicken:
            distance = abs(x - i) + abs(y - j)
            min_distance = min(min_distance, distance)
        sum_distance += min_distance
    return sum_distance

# 모든 가능한 치킨 집의 조합을 고려하여 최소 치킨 거리 계싼
def get_min_distance():
    min_distance = sys.maxsize
    for comb in combinations(position_chicken, m):
        distance = calculate_sum_distance(comb)
        min_distance = min(min_distance, distance)
    return min_distance


# 모든 집과 치킨 집의 위치 저장
for i in range(n):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            position_house.append((i, j))
        elif graph[i][j] == 2:
            position_chicken.append((i, j))

# 결과 출력
print(get_min_distance())

