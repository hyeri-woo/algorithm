import sys

f = open("test1.txt", "r")
n = int(f.readline())
a = [list(map(int, f.readline().split())) for _ in range(n)]

ans = sys.maxsize
visited = [False] * n

def dfs(start, now, value, cnt):
    global ans
    if cnt == n:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return
    if value >  ans:
        return
    for i in range(n):
        if not visited[i] and a[now][i]:
            visited[i] = True
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = False 

for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False
print(ans)