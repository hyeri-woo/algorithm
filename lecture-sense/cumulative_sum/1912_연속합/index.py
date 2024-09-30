# import sys
# input = sys.stdin.readline
f = open("test3.txt")
input = f.readline
n = int(input())
numbers = list(map(int, input().split()))

prefix = [0] * (n)
prefix[0] = numbers[0]
for i in range(1, n):
    prefix[i] = max(prefix[i-1] + numbers[i], numbers[i])

print(max(prefix))
