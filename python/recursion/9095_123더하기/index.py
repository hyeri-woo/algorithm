f = open("test1.txt", "r")
n = int(f.readline())
a = [int(f.readline()) for _ in range(n)]
dp = [0] * (max(a)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in a:
    print(dp[i])