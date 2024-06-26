import sys
import copy
from collections import deque
# input = sys.stdin.readline
f = open('test3.txt')
input = f.readline
n, m = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(n)]

# 바이러스가 퍼지는 과정
def bfs(graph):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    temp_graph = copy.deepcopy(graph)
    # 바이러스 위치를 큐에 삽입
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i, j))
    
    # 탐색 시작
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp_graph[nx][ny] == 0:  # 감염 가능 여부 확인
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))
    
    global answer
    count = 0
    for i in range(n):
        count += temp_graph[i].count(0)
        # print(temp_graph)
    answer = max(answer, count)

def makeWall(graph, count):
    if count == 3:
        bfs(graph)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:    # 벽 세우기 가능 여부 확인
                graph[i][j] = 1    # 벽을 세우고
                makeWall(graph, count + 1)  # 다시 두번째 벽 세움
                graph[i][j] = 0             # 다시 벽을 허문

answer = 0
makeWall(building, 0)
print(answer)