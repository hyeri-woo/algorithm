import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, m = map(int, input().split())
lectures = list(map(int, input().split()))
lectures.sort()

def is_valid_length(max_length):
    partial_sum = 0
    count = 1
    for l in lectures:
        if l + partial_sum > max_length:
            partial_sum = 0
            count += 1
        partial_sum += l
    if count <= m:
        return True
    return False

def search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if is_valid_length(mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

start = max(lectures)
end = sum(lectures)

print(search(start, end))