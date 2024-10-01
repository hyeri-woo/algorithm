# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

# 탑다운
# dp = [[-1]* 100_001 for _ in range(n+1)]
# def recur(idx, weight):
#     if weight > k:
#         return -1 * float('inf')
#     if idx == n:
#         return 0
#     if dp[idx][weight] != -1:
#         return dp[idx][weight]

#     dp[idx][weight] = max(recur(idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx + 1, weight))

#     return dp[idx][weight]

# print(recur(0, 0))

# 바텀업
dp = [[0]* (100_001) for _ in range(n+1)]
for idx in range(1, n):
    for weight in range(k + 1):
        # print(idx, weight)
        if weight < k:
            dp[idx][weight] = dp[idx - 1][weight]
        else:
            dp[idx][weight] = max(dp[idx - 1][weight + items[idx][0]] + items[idx][1], dp[idx - 1][weight])

print(max(max(d) for d in dp))