# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def recur(y, x):
    if y == m - 1 and x == n - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    route = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ey, ex = y + dy, x + dx
        if 0 <= ey < m and 0 <= ex < n:
            if graph[y][x] > graph[ey][ex]:
                route += recur(ey, ex)
    dp[y][x] = route
    return dp[y][x]

print(recur(0, 0))