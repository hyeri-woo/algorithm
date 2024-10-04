import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n = int(input())
point = list(int(input()) for _ in range(n))

if n == 1:  # 계단이 1개일 때
    print(point[0])
    sys.exit()
elif n == 2:  # 계단이 2개일 때
    print(point[0] + point[1])
    sys.exit()

dp = [0] * (n)
dp[0] = point[0]
dp[1] = point[0] + point[1]
dp[2] = max(point[0] + point[2], point[1] + point[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + point[i], dp[i-3] + point[i-1] + point[i])

print(dp)