import sys
# input = sys.stdin.readline
f = open('test2.txt')
input = f.readline
n, m = map(int, input().split())
daily = list(int(input()) for _ in range(n))

def diff_money(withdrawal_amount):
    curr = withdrawal_amount
    count = 1
    for amount in daily:
        if curr < amount:
            count += 1
            curr = withdrawal_amount
        curr -= amount 
    return count <= m
    

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if diff_money(mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

start = max(daily)
end = sum(daily)
print(binary_search(start, end))