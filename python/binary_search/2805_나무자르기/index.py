import sys
# input = sys.stdin.readline
f = open('test2.txt')
input = f.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total += i - mid
        
        if total >= target:
            result = mid  # 최댓값을 찾는 것이므로 조건을 만족하면 일단 저장
            start = mid + 1
        else:
            end = mid - 1
    
    return result

print(binary_search(tree, m, 1, max(tree)))