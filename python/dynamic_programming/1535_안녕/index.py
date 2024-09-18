import sys
# input = sys.stdin.readline
f = open('test6.txt')
input = f.readline
n = int(input())
health_list = list(map(int, input().split())) 
happy_list = list(map(int, input().split()))

dp = [0] * 101 # 체력 0 ~ 100까지의 최대 기쁨을 저장할 배열

# 각 사람에 대해
for i in range(n):
    # 체력 감소는 뒤에서부터 처리 (중복 인사 방지)
    for health in range(100, health_list[i], -1):
        # dp[health]: 인사하지 않는 경우와 인사하는 경우 중 큰 값 선택
        dp[health] = max(dp[health], dp[health - health_list[i]] + happy_list[i])

print(max(dp[1:]))