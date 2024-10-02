# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i): # i 기준 왼쪽에 있는 숫자까지 확인
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
