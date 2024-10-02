# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다!
# def recur(y, x):
#     point = 0
#     for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         ey, ex = y + dy, x + dx
#         if 0 <= ey < n and 0 <= ex < n:
#             if graph[y][x] < graph[ey][ex]:
#                 point = max(point, recur(ey, ex) + 1)
#     return point
    
# 재귀로 구현한 뒤 DP로 바꾼다
dp = [[0] * n for _ in range(n)]

def recur(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ey, ex = y + dy, x + dx
        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)
    return dp[y][x]


# 모든 점을 방문한다
for y in range(n):
    for x in range(n):
        recur(y, x)

print(max(map(max, dp)) + 1)
