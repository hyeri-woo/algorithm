# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

dp[0] = cost[0]

for i in range(1, n):
    # 빨간집을 골랐을때 i-1의 집이 초록이나 파랑 중 비용이 작은 값 저장
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록집을 골랐을때 i-1의 집이 빨강이나 파랑 중 비용이 작은 값 저장
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑집을 골랐을때 i-1의 집이 빨강이나 초록 중 비용이 작은 값 저장
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))