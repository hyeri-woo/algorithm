f = open("test1.txt", "r")
n = int(f.readline())
schedule = [list(map(int, f.readline().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])

print(dp[0])