import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, m = map(int, input().split())
lectures = list(map(int, input().split()))

print(n, m, lectures)