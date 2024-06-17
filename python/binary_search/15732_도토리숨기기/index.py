import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]
print(n, k, d, rules)