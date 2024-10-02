# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s, e = 0, n - 1
count = 0
remain = 0

while s <= e:
    if arr[e] >= x:
        count += 1
        e -= 1
        continue
    if s == e:
        remain += 1
        break
    if arr[s] + arr[e] >= x / 2:
        count += 1
        s += 1
        e -= 1
    else:
        s += 1
        remain += 1
   
print(count + remain // 3)