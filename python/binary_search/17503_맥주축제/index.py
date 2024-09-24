import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, m, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(k)]

def add_satification(degree):
    items = [item[0] for item in info if item[1] <= degree]
    items.sort(reverse=True)
    return sum(items[:n]) if len(items) >= n else 0

def search(start, end):
    result = float('inf')
    while start <= end:
        mid = (start + end) // 2
        sums = add_satification(mid)
        if sums < m:
            start = mid + 1
        else:
            result = min(result, mid)
            end = mid - 1
    return result

min_degree, max_degree = min([item[1] for item in info]), max([item[1] for item in info])
result = search(min_degree, max_degree)
if result > max_degree:
    print(-1)
else:
    print(result)