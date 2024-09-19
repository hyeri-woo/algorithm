import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline

# 입력
n_list = []
while True:
    n = input()
    if not n:
        break
    n_list.append(int(n))

# 문제 풀이
dp = [0] * (max(n_list) + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, len(dp)):
    dp[i] = dp[i-1] + 2*dp[i-2]

# 출력
for n in n_list:
    print(dp[n])