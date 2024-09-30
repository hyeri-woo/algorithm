# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n, h = map(int, input().split())

prefix = [0] * h

for i in range(n):
    l = int(input())
    # 석순
    if i % 2 == 0:
        prefix[0] += 1
        prefix[l] -= 1
    # 종유석
    else:
        prefix[h-l] += 1

for i in range(1, h):
    prefix[i] += prefix[i-1]

min_barrier = min(prefix)
count = prefix.count(min_barrier)
print(min_barrier, count)