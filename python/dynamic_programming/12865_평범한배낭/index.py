import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, k = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(n)]

# dp 초기화
dp = [0] * (k + 1)

for w, v in stuff:
    # 물건을 넣을 때, 뒤에서부터 앞으로 업데이트합니다.
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])