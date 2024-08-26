# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

# 입력
a, b, c, d, e, f = map(int, input().split())

# 문제 풀이
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            # 출력
            print(x, y)
            break