import sys
# input = sys.stdin.readline
f = open('test3.txt')
input = f.readline
n, m = map(int, input().split())

dp = [[1] * (max(n, m) + 1) for _ in range((max(n, m) + 1))]

for i in range(2, n+1):
    for j in range(2, m+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % 1_000_000_007

print(dp[n][m])