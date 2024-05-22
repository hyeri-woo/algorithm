import sys
input = sys.stdin.readline
f = open('test2.txt')
n = int(f.readline())

# dp 배열 초기화
dp = [[1] for _ in range(n + 1)]

# 연산을 통해 최솟값을 구함
for i in range(2, n + 1):
    # 이전 단계에서 최솟값을 구함
    min_steps = dp[i - 1] + [i]
    if i % 3 == 0:
        min_steps = min(min_steps, dp[i // 3] + [i], key=len)
    if i % 2 == 0:
        min_steps = min(min_steps, dp[i // 2] + [i], key=len)
    dp[i] = min_steps

# 결과 출력
print(len(dp[n]) - 1)
print(' '.join(map(str, reversed(dp[n]))))