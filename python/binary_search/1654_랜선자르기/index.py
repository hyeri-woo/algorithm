import sys
# input = sys.stdin.readline
f = open('test1.txt', 'r')
input = f.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

def match_num_cable(length, target):
    count = 0
    for l in lines:
        count += l // length
    if count >= target:
        return True
    return False

def search(start, end):
    result = start
    while start <= end:
        mid = (start + end) // 2
        is_match = match_num_cable(mid, n)
        if is_match:
            result = max(mid, result)
            start = mid + 1
        else:
            end = mid - 1
    return result

print(search(1, max(lines)))