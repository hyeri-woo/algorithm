# import sys
# input = sys.stdin.readline
f = open("test6.txt")
input = f.readline
n, m = map(int, input().split())
price = [list(map(int, input().split())) for _ in range(m)]

min_package = min(p[0] for p in price)
min_each = min(p[1] for p in price)

only_package = min_package*(n // 6 + 1)
both = min_package*(n // 6) + min_each*(n % 6)
only_each = min_each * n

print(min(only_package, both, only_each))