# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
interview = [list(map(int, input().split())) for _ in range(n)]

# # 탑다운 
dp = [-1] * (n+1)
# def recur(idx):
#     if idx == n:
#         return 0
#     if idx > n:
#         return -1 * float('inf')
#     if dp[idx] != -1:
#         return dp[idx]
#     # 상담을 받거나, 안 받거나, 그 중에서 더 많은 돈을 버는 경우를 dp에 저장
#     dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx + 1))

#     return dp[idx]
    
# print(recur(0))

# 바텀엄
dp = [0] * (n + 1)
for idx in range(n)[::-1]:
    # print(idx, interview[idx])
    if idx + interview[idx][0] > n:
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + interview[idx][0]] + interview[idx][1], dp[idx + 1])

print(max(dp))