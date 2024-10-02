# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

s, e = 0, n-1
count = 0
while s < e:
    sum = arr[s] + arr[e]
    if sum == x:
        count += 1
        s += 1
        e -= 1
    elif sum < x:
        s += 1
    else:
        e -= 1

print(count)