import sys

f = open("test3.txt", "r")
n = int(f.readline())
a = list(f.readline().split())

for i in range(n-1, 0, -1):
    if a[i-1]>a[i]:
        target = i-1
        break
else:
    print(-1)
    sys.exit()

for i in range(n-1, 0, -1):
    if a[target]>a[i]:
        a[target],a[i] = a[i],a[target]
        a = a[:target + 1] + sorted(a[target + 1:], reverse=True)
        print(*a)
        break