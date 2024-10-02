# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

m = list(input().strip())  # .strip()을 추가하여 개행 문자 제거
n = list(input().strip())

dp = [[0] * (len(n) + 1) for _ in range(len(m) + 1)]

for i in range(1, len(m) + 1):
    for j in range(1, len(n) + 1):
        if m[i-1] == n[j-1]:  # 마지막 문자가 같다면, 대각선 값을 들고와 +1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(m)][len(n)])