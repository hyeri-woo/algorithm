import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]

def count_acorn (box_num):
    total_acorns = 0
    for a, b, c in rules:
        if a <= box_num:
            total_acorns += (min(b, box_num) - a) // c + 1
    return total_acorns

def search(start, end):
    while start < end:
        mid = (start + end) // 2
        count = count_acorn(mid)
        if count >= d:
            end = mid
        else:
            start = mid + 1
    return start

start = 1
end = n

print(search(start, end))