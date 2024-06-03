import sys
# input = sys.stdin.readline
f = open('test2.txt')
input = f.readline
n = int(input())
budget = list(map(int, input().split()))
total = int(input())

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(budget, total, 1, max(budget)))