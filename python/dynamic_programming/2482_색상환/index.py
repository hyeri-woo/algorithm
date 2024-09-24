import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
mod = 1_000_000_003
n = int(input())
k = int(input())

dp = [[0] * 1001 for _ in range(1001)]

for i in range(n+1):
    dp[i][1] = i
    dp[i][0] = 1

for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % mod

print((dp[n - 1][k] + dp[n - 3][k - 1]) % mod)