# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n, k = map(int, input().split())
temp = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + temp[i]

answer = -1 * float('inf')
for i in range(0, n-k+1):
    answer = max(answer, prefix[i+k] - prefix[i])

print(answer)